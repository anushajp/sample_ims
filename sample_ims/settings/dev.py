from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ims_db',
        'USER': 'ims_admin',
        'PASSWORD': 'ims@2020',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'app_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': '/opt/sample_ims/logs/application.log',
        },
    },
    'loggers': {
        'application_log': {
            'handlers': ['app_file',],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}



# SUPPORT_EMAIL = 'jrny@jrnyon.com'
SUPPORT_EMAIL = 'anusha.prasanth10@gmail.com'