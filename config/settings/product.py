from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# AWS
ALLOWED_HOSTS = ['.elasticbeanstalk.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get("DATABASE_HOST"),
        'NAME': os.environ.get("DATABASE_NAME"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
        "USER": os.environ.get("DATABASE_USER"),
        "PORT": 5432,
    }
}


DEFAULT_FILE_STORAGE = 'config.custom_storages.UploadStorage'
STATICFILES_STORAGE = 'config.custom_storages.StaticStorage'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
# AWS_S3_OBJECT_PARAMETERS = {}
AWS_S3_CUSTOM_DOMAIN = "AWS_S3_CUSTOM_DOMAIN"
AWS_DEFAULT_ACL = 'public-read'

# AWS_S3_CUSTOM_DOMAIN = f"{os.environ.get('AWS_S3_CUSTOM_DOMAIN')}"
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"