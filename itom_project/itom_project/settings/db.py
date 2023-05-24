import os


DATABASE_NAMES = os.getenv('DATABASE_NAMES', 'shop-1,shop-2')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shop-default',
        'USER': os.getenv('DATABASE_USER', 'root'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'pwd123456'),
        'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.getenv('DATABASE_PORT', 3306),
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {'charset': 'utf8mb4', 'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'},
    },
}
for db_name in DATABASE_NAMES.split(','):
    DATABASES[db_name] = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_name,
        'USER': os.getenv('DATABASE_USER', 'root'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'pwd123456'),
        'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.getenv('DATABASE_PORT', 3306),
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {'charset': 'utf8mb4', 'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'},
    }
