from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': os.environ.get("DATABASE_HOST"),
#         'NAME': os.environ.get("DATABASE_NAME"),
#         "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
#         "USER": os.environ.get("DATABASE_USER"),
#         "PORT": 5432,
#     }
# }
