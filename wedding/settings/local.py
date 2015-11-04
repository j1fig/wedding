from .base import *

import warnings
warnings.filterwarnings(
    'error',
    r"DateTimeField .* received a naive datetime",
    RuntimeWarning,
    r'django\.db\.models\.fields'
)

if not DEBUG:
    ALLOWED_HOSTS = ['*']

LOCAL = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d '
                      '%(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'data_ins.tests': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
