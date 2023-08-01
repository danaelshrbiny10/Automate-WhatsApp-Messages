"""Django settings for config/settings/production.py project."""


from .base import *
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
# Caches Settings
# ______________________________________________________________________________


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-Automate_Whatsapp_API",
        "TIMEOUT": 60 * 15,  # 15 minutes cache timeout
    },
}


CACHE_MIDDLEWARE_SECONDS = 60 * 15  # 15 minutes cache timeout
CACHE_MIDDLEWARE_ALIAS = "default"
