import os
import dj_database_url

from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

# SSL Settings
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True

ADMINS = (
    ('Joao Figueiredo', 'joaonvfigueiredo@gmail.com'),
)

ALLOWED_HOSTS = [
    '.joao-e-paola.xyz',
    'ec2-52-30-42-82.eu-west-1.compute.amazonaws.com',
]

MEDIA_ROOT = os.getenv('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))
