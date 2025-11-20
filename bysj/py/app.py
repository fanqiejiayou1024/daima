from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import bcrypt
import jwt
import datetime
from functools import wraps
import os
import secrets
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

app = Flask(__name__)

# 配置信息
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['MYSQL_CONFIG'] = {
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', ''),
    'database': os.getenv('MYSQL_DATABASE', 'db_library'),
    'port': int(os.getenv('MYSQL_PORT', '3306'))
}

CORS(app)


def get_db_connection():
    """获取数据库连接"""
    try:
        connection = mysql.connector.connect(**app.config['MYSQL_CONFIG'])
        return connection
    except Error as e:
        print(f"数据库连接错误: {e}")
        return None


def token_required(f):
    """JWT token验证装饰器"""

    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token缺失'}), 401

        try:
            if token.startswith('Bearer '):
                token = token[7:]

            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = data['username']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token已过期'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': '无效Token'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


@app.route('/api/login', methods=['POST'])
def login():
    """用户登录接口"""
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({
                'success': False,
                'message': '用户名和密码不能为空'
            }), 400

        connection = get_db_connection()
        if not connection:
            return jsonify({
                'success': False,
                'message': '数据库连接失败'
            }), 500

        cursor = connection.cursor(dictionary=True)

        # 查询用户信息
        query = "SELECT * FROM user WHERE username = %s AND is_deleted = 'n'"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        if not user:
            cursor.close()
            connection.close()
            return jsonify({
                'success': False,
                'message': '用户不存在'
            }), 401

        # 验证密码
        if not bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            cursor.close()
            connection.close()
            return jsonify({
                'success': False,
                'message': '密码错误'
            }), 401

        # 生成JWT token
        token = jwt.encode({
            'username': user['username'],
            'user_type': user.get('user_type', 'user'),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'], algorithm='HS256')

        cursor.close()
        connection.close()

        return jsonify({
            'success': True,
            'message': '登录成功',
            'token': token,
            'user': {
                'id': user['id'],
                'username': user['username'],
                'user_type': user.get('user_type', 'user'),
                'name': user.get('name', '')
            }
        })

    except Exception as e:
        print(f"登录错误: {e}")
        return jsonify({
            'success': False,
            'message': '服务器内部错误'
        }), 500


@app.route('/api/register', methods=['POST'])
def register():
    """用户注册接口"""
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        name = data.get('name', '')
        user_type = data.get('user_type', 'user')

        if not username or not password:
            return jsonify({
                'success': False,
                'message': '用户名和密码不能为空'
            }), 400

        if len(password) < 6:
            return jsonify({
                'success': False,
                'message': '密码长度至少6位'
            }), 400

        connection = get_db_connection()
        if not connection:
            return jsonify({
                'success': False,
                'message': '数据库连接失败'
            }), 500

        cursor = connection.cursor()

        # 检查用户名是否已存在
        check_query = "SELECT id FROM user WHERE username = %s"
        cursor.execute(check_query, (username,))
        if cursor.fetchone():
            cursor.close()
            connection.close()
            return jsonify({
                'success': False,
                'message': '用户名已存在'
            }), 400

        # 加密密码
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # 插入新用户
        insert_query = """
                       INSERT INTO user (username, password, user_type, name, is_deleted)
                       VALUES (%s, %s, %s, %s, 'n') \
                       """
        cursor.execute(insert_query, (username, hashed_password, user_type, name))
        connection.commit()

        user_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return jsonify({
            'success': True,
            'message': '注册成功',
            'user_id': user_id
        })

    except Exception as e:
        print(f"注册错误: {e}")
        return jsonify({
            'success': False,
            'message': '服务器内部错误'
        }), 500


@app.route('/api/books', methods=['GET'])
@token_required
def get_books(current_user):
    """获取图书列表"""
    try:
        connection = get_db_connection()
        if not connection:
            return jsonify({'message': '数据库连接失败'}), 500

        cursor = connection.cursor(dictionary=True)

        # 获取查询参数
        search = request.args.get('search', '')
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        offset = (page - 1) * limit

        if search:
            query = """
                    SELECT b.*, c.name as category_name
                    FROM book b
                             LEFT JOIN category c ON b.category_id = c.id
                    WHERE b.title LIKE %s \
                       OR b.author LIKE %s \
                       OR b.isbn LIKE %s
                    ORDER BY b.id DESC LIMIT %s \
                    OFFSET %s \
                    """
            cursor.execute(query, (f'%{search}%', f'%{search}%', f'%{search}%', limit, offset))
        else:
            query = "SELECT * FROM book ORDER BY id DESC LIMIT %s OFFSET %s"
            cursor.execute(query, (limit, offset))

        books = cursor.fetchall()

        # 获取总数
        if search:
            count_query = "SELECT COUNT(*) as total FROM book WHERE title LIKE %s OR author LIKE %s OR isbn LIKE %s"
            cursor.execute(count_query, (f'%{search}%', f'%{search}%', f'%{search}%'))
        else:
            cursor.execute("SELECT COUNT(*) as total FROM book")

        total = cursor.fetchone()['total']

        cursor.close()
        connection.close()

        return jsonify({
            'success': True,
            'books': books,
            'total': total,
            'page': page,
            'limit': limit
        })

    except Exception as e:
        print(f"获取图书错误: {e}")
        return jsonify({
            'success': False,
            'message': '获取图书列表失败'
        }), 500


@app.route('/api/books', methods=['POST'])
@token_required
def add_book(current_user):
    """添加图书"""
    try:
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        isbn = data.get('isbn')
        publisher = data.get('publisher', '')
        publish_date = data.get('publish_date', '')
        stock = data.get('stock', 1)
        category_id = data.get('category_id')

        if not title or not author or not isbn:
            return jsonify({
                'success': False,
                'message': '书名、作者和ISBN不能为空'
            }), 400

        connection = get_db_connection()
        if not connection:
            return jsonify({
                'success': False,
                'message': '数据库连接失败'
            }), 500

        cursor = connection.cursor()

        # 检查ISBN是否已存在
        check_query = "SELECT id FROM book WHERE isbn = %s"
        cursor.execute(check_query, (isbn,))
        if cursor.fetchone():
            cursor.close()
            connection.close()
            return jsonify({
                'success': False,
                'message': 'ISBN已存在'
            }), 400

        insert_query = """
                       INSERT INTO book (title, author, isbn, publisher, publish_date, stock, category_id)
                       VALUES (%s, %s, %s, %s, %s, %s, %s) \
                       """
        cursor.execute(insert_query, (title, author, isbn, publisher, publish_date, stock, category_id))
        connection.commit()

        book_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return jsonify({
            'success': True,
            'message': '添加图书成功',
            'book_id': book_id
        })

    except Exception as e:
        print(f"添加图书错误: {e}")
        return jsonify({
            'success': False,
            'message': '添加图书失败'
        }), 500


@app.route('/api/books/<int:book_id>', methods=['PUT'])
@token_required
def update_book(current_user, book_id):
    """更新图书信息"""
    try:
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        isbn = data.get('isbn')
        publisher = data.get('publisher', '')
        publish_date = data.get('publish_date', '')
        stock = data.get('stock', 1)
        category_id = data.get('category_id')

        if not title or not author or not isbn:
            return jsonify({
                'success': False,
                'message': '书名、作者和ISBN不能为空'
            }), 400

        connection = get_db_connection()
        if not connection:
            return jsonify({
                'success': False,
                'message': '数据库连接失败'
            }), 500

        cursor = connection.cursor()

        # 检查ISBN是否已被其他图书使用
        check_query = "SELECT id FROM book WHERE isbn = %s AND id != %s"
        cursor.execute(check_query, (isbn, book_id))
        if cursor.fetchone():
            cursor.close()
            connection.close()
            return jsonify({
                'success': False,
                'message': 'ISBN已被其他图书使用'
            }), 400

        update_query = """
                       UPDATE book
                       SET title        = %s, \
                           author       = %s, \
                           isbn         = %s, \
                           publisher    = %s,
                           publish_date = %s, \
                           stock        = %s, \
                           category_id  = %s
                       WHERE id = %s \
                       """
        cursor.execute(update_query, (title, author, isbn, publisher, publish_date, stock, category_id, book_id))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({
            'success': True,
            'message': '更新图书成功'
        })

    except Exception as e:
        print(f"更新图书错误: {e}")
        return jsonify({
            'success': False,
            'message': '更新图书失败'
        }), 500


@app.route('/api/books/<int:book_id>', methods=['DELETE'])
@token_required
def delete_book(current_user, book_id):
    """删除图书"""
    try:
        connection = get_db_connection()
        if not connection:
            return jsonify({
                'success': False,
                'message': '数据库连接失败'
            }), 500

        cursor = connection.cursor()

        # 检查图书是否存在
        check_query = "SELECT id FROM book WHERE id = %s"
        cursor.execute(check_query, (book_id,))
        if not cursor.fetchone():
            cursor.close()
            connection.close()
            return jsonify({
                'success': False,
                'message': '图书不存在'
            }), 404

        delete_query = "DELETE FROM book WHERE id = %s"
        cursor.execute(delete_query, (book_id,))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({
            'success': True,
            'message': '删除图书成功'
        })

    except Exception as e:
        print(f"删除图书错误: {e}")
        return jsonify({
            'success': False,
            'message': '删除图书失败'
        }), 500


@app.route('/api/users', methods=['GET'])
@token_required
def get_users(current_user):
    """获取用户列表"""
    try:
        connection = get_db_connection()
        if not connection:
            return jsonify({'message': '数据库连接失败'}), 500

        cursor = connection.cursor(dictionary=True)

        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        offset = (page - 1) * limit

        query = """
                SELECT id, \
                       username, \
                       user_type, \
                       name, \
                       photo, \
                       is_deleted, \
                       created_at, \
                       updated_at
                FROM user
                WHERE is_deleted = 'n'
                ORDER BY id DESC LIMIT %s \
                OFFSET %s \
                """
        cursor.execute(query, (limit, offset))
        users = cursor.fetchall()

        cursor.execute("SELECT COUNT(*) as total FROM user WHERE is_deleted = 'n'")
        total = cursor.fetchone()['total']

        cursor.close()
        connection.close()

        return jsonify({
            'success': True,
            'users': users,
            'total': total,
            'page': page,
            'limit': limit
        })

    except Exception as e:
        print(f"获取用户错误: {e}")
        return jsonify({
            'success': False,
            'message': '获取用户列表失败'
        }), 500


@app.route('/api/users/<int:user_id>', methods=['PUT'])
@token_required
def update_user(current_user, user_id):
    """更新用户信息"""
    try:
        data = request.get_json()
        username = data.get('username')
        name = data.get('name')
        user_type = data.get('user_type')
        photo = data.get('photo')

        if not username:
            return jsonify({
                'success': False,
                'message': '用户名不能为空'
            }), 400

        connection = get_db_connection()
        if not connection:
            return jsonify({
                'success': False,
                'message': '数据库连接失败'
            }), 500

        cursor = connection.cursor()

        # 检查用户名是否已被其他用户使用
        check_query = "SELECT id FROM user WHERE username = %s AND id != %s"
        cursor.execute(check_query, (username, user_id))
        if cursor.fetchone():
            cursor.close()
            connection.close()
            return jsonify({
                'success': False,
                'message': '用户名已存在'
            }), 400

        update_query = """
                       UPDATE user
                       SET username   = %s, \
                           name       = %s, \
                           user_type  = %s, \
                           photo      = %s, \
                           updated_at = NOW()
                       WHERE id = %s \
                       """
        cursor.execute(update_query, (username, name, user_type, photo, user_id))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({
            'success': True,
            'message': '更新用户成功'
        })

    except Exception as e:
        print(f"更新用户错误: {e}")
        return jsonify({
            'success': False,
            'message': '更新用户失败'
        }), 500


@app.route('/api/users/<int:user_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, user_id):
    """删除用户（软删除）"""
    try:
        connection = get_db_connection()
        if not connection:
            return jsonify({
                'success': False,
                'message': '数据库连接失败'
            }), 500

        cursor = connection.cursor()

        # 检查用户是否存在
        check_query = "SELECT id FROM user WHERE id = %s"
        cursor.execute(check_query, (user_id,))
        if not cursor.fetchone():
            cursor.close()
            connection.close()
            return jsonify({
                'success': False,
                'message': '用户不存在'
            }), 404

        # 软删除
        delete_query = "UPDATE user SET is_deleted = 'y', updated_at = NOW() WHERE id = %s"
        cursor.execute(delete_query, (user_id,))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({
            'success': True,
            'message': '删除用户成功'
        })

    except Exception as e:
        print(f"删除用户错误: {e}")
        return jsonify({
            'success': False,
            'message': '删除用户失败'
        }), 500


@app.route('/api/categories', methods=['GET'])
@token_required
def get_categories(current_user):
    """获取分类列表"""
    try:
        connection = get_db_connection()
        if not connection:
            return jsonify({'message': '数据库连接失败'}), 500

        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM category ORDER BY name"
        cursor.execute(query)
        categories = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify({
            'success': True,
            'categories': categories
        })

    except Exception as e:
        print(f"获取分类错误: {e}")
        return jsonify({
            'success': False,
            'message': '获取分类列表失败'
        }), 500


@app.route('/api/borrow', methods=['POST'])
@token_required
def borrow_book(current_user):
    """借阅图书"""
    try:
        data = request.get_json()
        book_id = data.get('book_id')
        user_id = data.get('user_id')

        if not book_id or not user_id:
            return jsonify({
                'success': False,
                'message': '图书ID和用户ID不能为空'
            }), 400

        connection = get_db_connection()
        if not connection:
            return jsonify({
                'success': False,
                'message': '数据库连接失败'
            }), 500

        cursor = connection.cursor(dictionary=True)

        # 检查图书是否存在且有库存
        book_query = "SELECT * FROM book WHERE id = %s"
        cursor.execute(book_query, (book_id,))
        book = cursor.fetchone()

        if not book:
            cursor.close()
            connection.close()
            return jsonify({
                'success': False,
                'message': '图书不存在'
            }), 404

        if book['stock'] <= 0:
            cursor.close()
            connection.close()
            return jsonify({
                'success': False,
                'message': '图书库存不足'
            }), 400

        # 检查用户是否存在
        user_query = "SELECT id FROM user WHERE id = %s AND is_deleted = 'n'"
        cursor.execute(user_query, (user_id,))
        if not cursor.fetchone():
            cursor.close()
            connection.close()
            return jsonify({
                'success': False,
                'message': '用户不存在'
            }), 404

        # 插入借阅记录
        borrow_query = """
                       INSERT INTO borrow_record (user_id, book_id, borrow_date, status)
                       VALUES (%s, %s, %s, 'borrowed') \
                       """
        borrow_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(borrow_query, (user_id, book_id, borrow_date))

        # 更新图书库存
        update_stock_query = "UPDATE book SET stock = stock - 1 WHERE id = %s"
        cursor.execute(update_stock_query, (book_id,))

        connection.commit()
        record_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return jsonify({
            'success': True,
            'message': '借阅成功',
            'record_id': record_id
        })

    except Exception as e:
        print(f"借阅图书错误: {e}")
        return jsonify({
            'success': False,
            'message': '借阅图书失败'
        }), 500


@app.route('/api/borrow/return', methods=['POST'])
@token_required
def return_book(current_user):
    """归还图书"""
    try:
        data = request.get_json()
        record_id = data.get('record_id')

        if not record_id:
            return jsonify({
                'success': False,
                'message': '借阅记录ID不能为空'
            }), 400

        connection = get_db_connection()
        if not connection:
            return jsonify({
                'success': False,
                'message': '数据库连接失败'
            }), 500

        cursor = connection.cursor(dictionary=True)

        # 检查借阅记录是否存在
        record_query = "SELECT * FROM borrow_record WHERE id = %s AND status = 'borrowed'"
        cursor.execute(record_query, (record_id,))
        record = cursor.fetchone()

        if not record:
            cursor.close()
            connection.close()
            return jsonify({
                'success': False,
                'message': '借阅记录不存在或已归还'
            }), 404

        # 更新借阅记录状态
        return_query = """
                       UPDATE borrow_record
                       SET return_date = %s, \
                           status      = 'returned'
                       WHERE id = %s \
                       """
        return_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(return_query, (return_date, record_id))

        # 更新图书库存
        update_stock_query = "UPDATE book SET stock = stock + 1 WHERE id = %s"
        cursor.execute(update_stock_query, (record['book_id'],))

        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({
            'success': True,
            'message': '归还成功'
        })

    except Exception as e:
        print(f"归还图书错误: {e}")
        return jsonify({
            'success': False,
            'message': '归还图书失败'
        }), 500


@app.route('/api/borrow/records', methods=['GET'])
@token_required
def get_borrow_records(current_user):
    """获取借阅记录"""
    try:
        connection = get_db_connection()
        if not connection:
            return jsonify({'message': '数据库连接失败'}), 500

        cursor = connection.cursor(dictionary=True)

        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        offset = (page - 1) * limit

        query = """
                SELECT br.*, u.username, u.name as user_name, b.title, b.author, b.isbn
                FROM borrow_record br
                         JOIN user u ON br.user_id = u.id
                         JOIN book b ON br.book_id = b.id
                ORDER BY br.borrow_date DESC LIMIT %s \
                OFFSET %s \
                """
        cursor.execute(query, (limit, offset))
        records = cursor.fetchall()

        cursor.execute("SELECT COUNT(*) as total FROM borrow_record")
        total = cursor.fetchone()['total']

        cursor.close()
        connection.close()

        return jsonify({
            'success': True,
            'records': records,
            'total': total,
            'page': page,
            'limit': limit
        })

    except Exception as e:
        print(f"获取借阅记录错误: {e}")
        return jsonify({
            'success': False,
            'message': '获取借阅记录失败'
        }), 500


@app.route('/api/stats', methods=['GET'])
@token_required
def get_stats(current_user):
    """获取系统统计信息"""
    try:
        connection = get_db_connection()
        if not connection:
            return jsonify({'message': '数据库连接失败'}), 500

        cursor = connection.cursor(dictionary=True)

        # 图书总数
        cursor.execute("SELECT COUNT(*) as total_books FROM book")
        total_books = cursor.fetchone()['total_books']

        # 用户总数
        cursor.execute("SELECT COUNT(*) as total_users FROM user WHERE is_deleted = 'n'")
        total_users = cursor.fetchone()['total_users']

        # 借阅中图书数量
        cursor.execute("SELECT COUNT(*) as borrowing_books FROM borrow_record WHERE status = 'borrowed'")
        borrowing_books = cursor.fetchone()['borrowing_books']

        # 库存不足的图书数量
        cursor.execute("SELECT COUNT(*) as low_stock_books FROM book WHERE stock < 5")
        low_stock_books = cursor.fetchone()['low_stock_books']

        cursor.close()
        connection.close()

        return jsonify({
            'success': True,
            'stats': {
                'total_books': total_books,
                'total_users': total_users,
                'borrowing_books': borrowing_books,
                'low_stock_books': low_stock_books
            }
        })

    except Exception as e:
        print(f"获取统计信息错误: {e}")
        return jsonify({
            'success': False,
            'message': '获取统计信息失败'
        }), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """健康检查接口"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.utcnow().isoformat()
    })


if __name__ == '__main__':
    # 检查数据库连接和表结构
    try:
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()

            # 检查表是否存在
            cursor.execute("SHOW TABLES LIKE 'user'")
            user_table_exists = cursor.fetchone()

            cursor.execute("SHOW TABLES LIKE 'book'")
            book_table_exists = cursor.fetchone()

            cursor.execute("SHOW TABLES LIKE 'category'")
            category_table_exists = cursor.fetchone()

            cursor.execute("SHOW TABLES LIKE 'borrow_record'")
            borrow_table_exists = cursor.fetchone()

            print("数据库表检查结果:")
            print(f"user表: {'存在' if user_table_exists else '不存在'}")
            print(f"book表: {'存在' if book_table_exists else '不存在'}")
            print(f"category表: {'存在' if category_table_exists else '不存在'}")
            print(f"borrow_record表: {'存在' if borrow_table_exists else '不存在'}")

            connection.close()
    except Exception as e:
        print(f"数据库检查错误: {e}")

    app.run(debug=True, host='0.0.0.0', port=5000)
