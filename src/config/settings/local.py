"""Django settings for config/settings/local.py project."""

from .base import *


# GENERAL SETTINGS
# ______________________________________________________________________________


# ______________________________________________________________________________
# DEBUG SETTINGS
# ______________________________________________________________________________

"""
https://docs.djangoproject.com/en/dev/ref/settings/#debug
SECURITY WARNING: don't run with debug turned on in production!
"""

DEBUG = os.getenv("DEBUG", "False") == "True"

# ______________________________________________________________________________
# SECRET KEY SETTINGS
# ______________________________________________________________________________

"""
https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECURITY WARNING: keep the secret key used in production secret!
"""

SECRET_KEY = os.getenv("SECRET_KEY")

# ______________________________________________________________________________
# SECRET KEY SETTINGS
# ______________________________________________________________________________

"""
https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
"""
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1",'*']


CSRF_TRUSTED_ORIGINS = ["https://*.127.0.0.1", "http://localhost:8000","https://localhost:8000", "https://127.0.0.1:8000", "http://127.0.0.1:8000"]
