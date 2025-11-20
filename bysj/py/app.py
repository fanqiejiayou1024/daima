from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# 数据库连接配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'fanqie1024@X',
    'database': 'your_database'
}

def get_db_connection():
    return pymysql.connect(**db_config)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(sql, (data['name'], data['email']))
    conn.commit()
    user_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return jsonify({'id': user_id}), 201
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)
if __name__ == '__main__':
    app.run(debug=True)
