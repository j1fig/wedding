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
    ('Joao Figueiredo', 'joao.figueiredo@brain-e.pt'),
)

ALLOWED_HOSTS = [
    '.joao-e-paola.xyz',
]


# Database
db_config = dj_database_url.config(env='OPENSHIFT_POSTGRESQL_DB_URL')
db_config['NAME'] = os.environ.get('PGDATABASE')

DATABASES = {
    'default': db_config,
}

# Media files
MEDIA_ROOT = os.path.join(os.getenv('OPENSHIFT_DATA_DIR'), 'media')

# Static files (CSS, JavaScript, Images)
# Since BASE_DIR='/wsgi/openshift/settings',
# set STATIC_ROOT to be '/wsgi/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', '..', 'static')
