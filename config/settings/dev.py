from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-7l517b+9)md2lrymx@7ahv5dk56zsym9mnf#wxye+=ln&b96hp"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["0.0.0.0"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "pepe",
        "USER": "pepe",
        "PASSWORD": "pepe",
        "HOST": "db",
        "PORT": "5432",
    },
}
