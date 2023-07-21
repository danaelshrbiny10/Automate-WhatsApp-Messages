"""Django settings for config/settings/base.py project."""


from pathlib import Path
import os
import sys
from dotenv import load_dotenv


load_dotenv()


# GENERAL SETTINGS
# ______________________________________________________________________________


# ______________________________________________________________________________
# BASE DIR SETTINGS
# ______________________________________________________________________________

""" Build paths inside the project like this: BASE_DIR / 'subdir'."""

BASE_DIR = Path(__file__).resolve().parent.parent

# src/
sys.path.append(BASE_DIR / "src")

# ______________________________________________________________________________
# DEBUG SETTINGS
# ______________________________________________________________________________

"""
https://docs.djangoproject.com/en/dev/ref/settings/#debug
SECURITY WARNING: don't run with debug turned on in production!
"""

DEBUG = os.getenv("DEBUG", "False") == "True"

# ______________________________________________________________________________
# Internationalization SETTINGS
# ______________________________________________________________________________

"""https://docs.djangoproject.com/en/4.1/topics/i18n/"""

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# ______________________________________________________________________________
# DATABASE SETTINGS
# ______________________________________________________________________________

"""https://docs.djangoproject.com/en/4.1/ref/settings/#databases"""

DATABASES = {
    "default": {
        "ENGINE": os.getenv("ENGINE"),
        "NAME": os.getenv("NAME"),
        "USER": os.getenv("USER"),
        "PASSWORD": os.getenv("PASSWORD"),
        "HOST": os.getenv("HOST"),
        "PORT": os.getenv("PORT"),
    }
}


# ______________________________________________________________________________
# URLS SETTINGS
# ______________________________________________________________________________

"""https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf"""

ROOT_URLCONF = "config.urls"

"""https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application"""

WSGI_APPLICATION = "config.wsgi.application"


# ______________________________________________________________________________
# Application definition
# ______________________________________________________________________________

DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "autoslug",
    "drf_yasg",
    "django_celery_results",
    "django_celery_beat",
]

LOCAL_APPS = ["API", "core", "account"]

""" https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps"""
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ______________________________________________________________________________
# REST FRAMEWORK
# ______________________________________________________________________________

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

# ______________________________________________________________________________
# Password validation
# ______________________________________________________________________________

"""https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators"""

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ______________________________________________________________________________
# MIDDLEWARE SETTINGS
# ______________________________________________________________________________

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ______________________________________________________________________________
# Static files (CSS, JavaScript, Images)
# ______________________________________________________________________________

"""https://docs.djangoproject.com/en/4.1/howto/static-files/"""

STATIC_URL = "static/"

# ______________________________________________________________________________
# TEMPLATES
# ______________________________________________________________________________


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ______________________________________________________________________________
# Default primary key field type
# ______________________________________________________________________________

"""https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field"""

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ______________________________________________________________________________
# SWAGGER SETTINGS
# ______________________________________________________________________________

SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": False,
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}
    },
}

# ______________________________________________________________________________
# AUTHENTICATION BACKENDS
# ______________________________________________________________________________


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]


# ______________________________________________________________________________
# CELERY SETTINGS SETTINGS
# ______________________________________________________________________________

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")
CELERY_ACCEPT_CONTENT = os.getenv("CELERY_ACCEPT_CONTENT")
CELERY_RESULT_SERIALIZER = os.getenv("CELERY_RESULT_SERIALIZER")
CELERY_TASK_SERIALIZER = os.getenv("CELERY_TASK_SERIALIZER")
CELERY_TIMEZONE = os.getenv("CELERY_TIMEZONE")
CELERY_REDIS_RETRY_DELAY = 5

# ______________________________________________________________________________
# CELERY BEAT SETTINGS
# ______________________________________________________________________________

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"


# ______________________________________________________________________________
# CORS URLS REGEX SETTINGS
# ______________________________________________________________________________

"""django-cors-headers - https://github.com/adamchainz/django-cors-headers#setup"""

CORS_URLS_REGEX = os.getenv("CORS_URLS_REGEX")

# ______________________________________________________________________________
# JWT AUTH SETTINGS
# ______________________________________________________________________________

JWT_AUTH = {
    "JWT_SECRET_KEY": os.getenv("JWT_SECRET_KEY"),
    "JWT_ALGORITHM": os.getenv("JWT_ALGORITHM"),
    "JWT_EXPIRATION_DELTA": os.getenv("JWT_EXPIRATION_DELTA"),
    "JWT_ALLOW_REFRESH": os.getenv("JWT_ALLOW_REFRESH"),
    "JWT_REFRESH_EXPIRATION_DELTA": os.getenv("JWT_REFRESH_EXPIRATION_DELTA"),
}