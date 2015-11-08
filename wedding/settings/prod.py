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
]

