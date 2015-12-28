
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