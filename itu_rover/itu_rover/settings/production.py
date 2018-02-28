from .base import *

ALLOWED_HOSTS = [config('HOST_NAME')]

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_root')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media_root')
MEDIA_URL = '/media/'
