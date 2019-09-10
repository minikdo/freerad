from .base import *  # noqa

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': get_secret('DB_ENGINE'),
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('DB_USER'),
        'HOST': get_secret('DB_HOST'),
        'PASSWORD': get_secret('DB_PASS'),
    }
}

ALLOWED_HOSTS += ['freerad']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
