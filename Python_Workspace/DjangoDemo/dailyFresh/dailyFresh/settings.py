"""
Django settings for dailyFresh project.

Generated by 'django-admin startproject' using Django 1.8.2.

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
SECRET_KEY = '*-guyh6r-*x^z3ip%6ojaqs1qi)$u(9s*0yjex!f&js5uguh_%'

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
    'apps.cart',   # 购物车模块
    'apps.goods',  # 商品模块
    'apps.order',  # 订单模块
    'apps.user',   # 用户模块
    'tinymce',     # 富文本编辑器
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

ROOT_URLCONF = 'dailyFresh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dailyFresh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dailyfresh',
        'USER': 'root',
        'PASSWORD': 'lixuan',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# django认证系统使用的模型类
# 否则在迁移时，报错 fields.E304
AUTH_USER_MODEL = 'user.User'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 富文本编辑器的配置
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',  # 主题，advanced代表有高级功能
    'width': 600,         # 编辑器的宽
    'height': 400,        # 编辑器的高
}

# 发送邮件配置，163邮箱为例
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# # smtp服务地址
# EMAIL_HOST = 'smtp.163.com'
# EMAIL_PORT = 25
# # 发送邮件的邮箱
# EMAIL_HOST_USER = 'lixuan_gdut@163.com'
# # 客户端授权码
# EMAIL_HOST_PASSWORD = 'shisan19960706'
# # 收件人看到的发件人
# EMAIL_FROM = '天天生鲜<lixuan_gdut@163.com>'

# qq邮箱
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# smtp服务地址
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
# 开启ssl加密
# EMAIL_USE_SSL = True
# 发送邮件的邮箱
EMAIL_HOST_USER = '525868229@qq.com'
# 客户端授权码
EMAIL_HOST_PASSWORD = 'kmyttjmruhvtbidc'
# 收件人看到的发件人
EMAIL_FROM = '天天生鲜<525868229@qq.com>'

# 使用redis做缓存的配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/3",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 配置session存储，保存在缓存(redis)中
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# 未登录时请求某个页面(需要登录才能显示)跳转到的页面
LOGIN_URL = '/user/login'

# 设置Django调用的文件存储类
DEFAULT_FILE_STORAGE = 'utils.fdfs.storage.FdfsStorage'

# 设置FastDFS使用的client.conf文件路径
FDFS_CLIENT_CONF_PATH = './utils/fdfs/client.conf'

# 设置FastDFS存储服务器上的Nginx的ip和端口号
FDFS_NGINX_URL = 'http://127.0.0.1:8888/'