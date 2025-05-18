import os

from pathlib import Path
from decouple import Config, RepositoryEnv

BASE_DIR = Path(__file__).resolve().parent.parent

config_global = Config(RepositoryEnv(BASE_DIR / 'conf/env/.env'))
# config_conf = Config(RepositoryEnv(BASE_DIR / 'conf/env/.env.conf'))
# config_db = Config(RepositoryEnv(BASE_DIR / 'conf/env/.env.database'))

SECRET_KEY = config_global('SECRET_KEY')
DEBUG = config_global('DEBUG')

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'drf_spectacular',
    'rest_framework',

    'apps.core',
    'apps.api',
    'apps.customers',
    'apps.room',
    'apps.additional',
    'apps.office',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'string_if_invalid': "-",
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'banco' / 'api.sqlite3',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}


SPECTACULAR_SETTINGS = {
    'TITLE': 'backend-API-tests',
    'DESCRIPTION': 'Documentação para projeto da faculdade de Testes',
    'VERSION': 'v1',
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config_db('DB_NAME'),
#         'USER': config_db('DB_USER'),
#         'PASSWORD': config_db('DB_PASSWORD'),
#         'HOST': config_db('DB_HOST'),
#         'PORT': config_db('DB_PORT', cast=int),
#     }
# }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'customers.Customers'
