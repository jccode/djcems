
from settings import *

DEBUG = TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'refiredb',
        'USER': 'refire',
        'PASSWORD': '1q2w3e',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

ALLOWED_HOSTS = ['127.0.0.1','112.74.93.116','10.116.12.125',]

ADMINS = (
    ("Jessie", "492429624@qq.com"),
)

MANAGERS = (
    ("Jessie", "492429624@qq.com"),
)

# Cache

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


CORS_ORIGIN_WHITELIST += (
    '112.74.93.116',
    '10.116.12.125',
)
