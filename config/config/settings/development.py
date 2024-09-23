from .base import *

DEBUG = True

#database config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#override installed Apps
INSTALLED_APPS += [
    'weblog.apps.WeblogConfig'
]