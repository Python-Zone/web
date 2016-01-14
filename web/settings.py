# -*- coding: utf-8 -*-
"""
Django settings for PythonZone project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third Party Apps
    'compressor',
    'captcha',
    'ckeditor',
    'ckeditor_uploader',
    #'ckeditor_uploader',
    # My Apps
    'web',
    'users',
    'topics',
    'wiki',
    'jobs',
    'sites',
    'weixin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'web.context_processors.global_stats'
            ],
        },
    },
]

WSGI_APPLICATION = 'web.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'NAME': 'pythonzone',
        'USER': 'root',
        'PASSWORD': '',
        'OPTIONS':{
            'charset':'utf8mb4',
        },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

#USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True

LOGIN_URL = '/users/signin/'

# custom user model
AUTH_USER_MODEL = 'users.User'

# wechat config
WEIXIN = {
    "WEIXIN_TOKEN": "",
    "WEIXIN_APP_ID": "",
    "WEIXIN_APP_SECRET": "",
    "WEIXIN_ENCODING_AES_KEY": ""
}

# 七牛开发者key
QINIU_CONFIG = {
    "ACCESS_KEY": "",
    "SECRET_KEY": "",
    "BUCKET": "",
    "DOMAIN":""
}
QINIU_ACCESS_KEY = QINIU_CONFIG['ACCESS_KEY']
QINIU_SECRET_KEY = QINIU_CONFIG['SECRET_KEY']
QINIU_BUCKET_NAME = QINIU_CONFIG['BUCKET']
QINIU_BUCKET_DOMAIN = QINIU_CONFIG['DOMAIN']
DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuStorage'
# 富文本编辑器ckeditor配置
CKEDITOR_CONFIGS = {
    'default': {
        'language': 'zh-cn',
        'skin': 'moono',
        'toolbar_YouCustomToolbarConfig': [
            {'name': 'document', 'items': ['Bold', 'Italic', '-', 'NumberedList', 'BulletedList', 'Blockquote', '-',
                                           'Link', 'Image', 'Table', '-', 'CodeSnippet','-', 'Source', 'Preview', 'Maximize']
            }
        ],
        'toolbar': 'YouCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        'height': 300,
        'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                # you extra plugins here
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                # 'devtools',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath',
                'codesnippet'
            ])
    },
    'reply': {
        'language': 'zh-cn',
        'skin': 'moono',
        'toolbar_YouCustomToolbarConfig': [
            {'name': 'document', 'items': ['Bold', 'Italic', '-', 'NumberedList', 'BulletedList', 'Blockquote', '-',
                                           'Link', 'Image', 'Table', '-', 'CodeSnippet','-', 'Source', 'Preview', 'Maximize']
            }
        ],
        'toolbar': 'YouCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        'height': 100,
        'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                # you extra plugins here
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                # 'devtools',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath',
                'codesnippet'
            ])
    }
}

MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_BROWSE_SHOW_DIRS = True
#CKEDITOR_RESTRICT_BY_USER = True

from django.contrib import messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# websocket
WEBSOCKET_HOST = "localhost"
WEBSOCKET_PORT = 3000

## Import local settings
try:
    from local_settings import *
except ImportError:
    import sys, traceback
    sys.stderr.write("Warning: Can't find the file 'local_settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.stderr.write("\nFor debugging purposes, the exception was:\n\n")
    traceback.print_exc()
