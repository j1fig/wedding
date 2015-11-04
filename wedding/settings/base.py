"""
Django settings for openshift project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Database
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(),
}

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'core',
    'home',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

SITE_ID = 1
ROOT_URLCONF = 'wedding.urls'
WSGI_APPLICATION = 'wedding.wsgi.application'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Lisbon'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', 'English'),
    ('pt', 'Portuguese'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-MEDIA_ROOT
MEDIA_ROOT = os.getenv('MEDIA_ROOT_DIR')
