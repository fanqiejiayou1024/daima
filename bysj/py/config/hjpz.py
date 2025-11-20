import os
from dotenv import load_dotenv

# 加载.env文件中的环境变量
load_dotenv()

class Config:
    """基础配置类"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'fanqie1024@X')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'db_library')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', '3306'))

class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True

class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False

# 根据环境变量选择配置
env = os.getenv('FLASK_ENV', 'development')
if env == 'production':
    config = ProductionConfig
else:
    config = DevelopmentConfig

# 使用方法示例
if __name__ == '__main__':
    print(f"数据库主机: {config.MYSQL_HOST}")
    print(f"数据库名称: {config.MYSQL_DATABASE}")
    print(f"调试模式: {config.DEBUG}")
