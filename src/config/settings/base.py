"""Django settings for config/settings/base.py project."""


from datetime import timedelta
from pathlib import Path
import os
from dotenv import load_dotenv


load_dotenv()


# GENERAL SETTINGS
# ______________________________________________________________________________


# ______________________________________________________________________________
# BASE DIR SETTINGS
# ______________________________________________________________________________

""" Build paths inside the project like this: BASE_DIR / 'subdir'."""

BASE_DIR = Path(__file__).resolve().parent.parent

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

LANGUAGES = [
    ("en", "English"),
    ("fr", "French"),
    ("ar", "Arabic"),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

LANGUAGE_CODE = "en"
USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = "UTC"

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
        "HOST": os.getenv("HOST", "127.0.0.1"),
        "PORT": os.getenv("PORT", "5432"),
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
    "API.middleware.LogUnhandledExceptionMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

# ______________________________________________________________________________
# Static files (CSS, JavaScript, Images)
# ______________________________________________________________________________

"""https://docs.djangoproject.com/en/4.1/howto/static-files/"""

STATIC_URL = "/static/"
STATIC_ROOT = "static"

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

# Set Celery to use eager mode during testing
CELERY_TASK_ALWAYS_EAGER = True

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
# SECRET KEY SETTINGS
# ______________________________________________________________________________

"""
https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECURITY WARNING: keep the secret key used in production secret!
"""

SECRET_KEY = os.getenv("SECRET_KEY")

# ______________________________________________________________________________
# JWT AUTH SETTINGS
# ______________________________________________________________________________

JWT_AUTH = {
    "JWT_SECRET_KEY": SECRET_KEY,
    "JWT_ALGORITHM": "HS256",
    "JWT_EXPIRATION_DELTA": timedelta(days=1),
    "JWT_ALLOW_REFRESH": True,
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=7),
}

# ______________________________________________________________________________
# Logging and Error Handling SETTINGS
# ______________________________________________________________________________


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "app.log",
            "formatter": "standard",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": "INFO",
        },
        "your_app_name": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
        },
    },
}
