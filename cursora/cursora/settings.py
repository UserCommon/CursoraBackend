"""
Django settings for cursora project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import datetime
from datetime import timedelta
import psycopg2
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1%34@1pbxmgjebkk+ju($#p@-h-dct2kyss(13vw&qmipxb@b='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
CORS_ORIGIN_WHITELIST = [
    'http://192.168.0.106:8080',
    'http://localhost:8080'
] # If this is used, then not need to use `CORS_ORIGIN_ALLOW_ALL = True`
CORS_ORIGIN_REGEX_WHITELIST = [
    'http://192.168.0.106:8080',
    'http://localhost:8080'
]



# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'main',
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'djoser',
    'rest_framework.authtoken',
#    'rest_framework.jwt.authentication.JWTAuthentication',
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cursora.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cursora.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cursoradb',
        'USER': 'cursora',
        'PASSWORD': 'silvergold3',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

DATE_FORMAT = 'd E Y'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
#        'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.AllowAny',
#        'rest_framework.permissions.IsAuthenticated'
    ),
#    'PAGE_SIZE': 25,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
     #  'rest_framework.authentication.BasicAuthentication',
     #   'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework_json_api.pagination.PageNumberPagination',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
        'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DATETIME_FORMAT': "%d.%m.%Y %H:%M:%S",
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# smtp
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'cursoramailer@gmail.com'
EMAIL_HOST_PASSWORD = 'silvergold3'
EMAIL_PORT = 587

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

DOMAIN = ("localhost:8080")
SITE_NAME = ("Cursora")

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'recovery/new_password/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'verification/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {},
}
