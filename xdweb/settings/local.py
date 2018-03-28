from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'id9=_@7yxrfvmtfw2p5bx+t6!)_o4-(u8l(#j(zblhv569c_u&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_xdblog_new',
        'HOST': '192.168.100.1',
        'PORT': '3306',
        'USER': 'webapp',
        'PASSWORD': 'web123456app',
    }
}

# Cache
# cache 配置为Redis Backends
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

"""
自定义变量
"""
# 导航【技术杂谈】分类id列表
NAV_JSZT_CATEGORY = (1, 2, 3, 4, 7, 8)
# 导航【生活随笔】分类id列表
NAV_SHSB_CATEGORY = (5, 6)
# 分页，每页显示记录条数
PER_PAGE = 2

# 允许上传文件类型['jpg', 'png', 'jpeg']
ALLOW_SUFFIX = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'txt', 'html']

# 网站基本信息
SITE_NAME = u'释道灵夕.Blog――江南墨卷'
SITE_DESC = u'天将降大任于是人也，必先苦其心志，劳其筋骨，饿其体肤，空乏其身，行拂乱其所为，所以动心忍性，曾益其所不能。'
SITE_KEYWORDS = u'运维，开发，Linux，数据库'
SITE_BEIAN = u'粤ICP备11111111号'
PRO_EMAIL = u'name@163.com'

