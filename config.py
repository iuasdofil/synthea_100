import os

CONFIG = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('HOST'),
    'port': os.getenv('PORT', 5432),
    'database': os.getenv('DATABASE')
}
