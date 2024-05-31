class Config:
    MYSQL_HOST = 'db'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'example'
    MYSQL_DB = 'mydatabase'
    SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
