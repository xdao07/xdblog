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

# 自定义日志输出信息
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {  # 定义日志格式模板
#         'standard': {
#             # 2017-11-10 12:51:19,888 [Thread-1:6523] [xdblog.views:33] [views:index] [ERROR]- [Errno 2] No such file or directory: 'logo1.jpg'
#             'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] '
#                       '[%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
#
#     },
#     'filters': {  # Filter 用于对从logger 传递给handler 的日志记录进行额外的控制。
#     },
#     'handlers': {
#         'mail_admins': {  # 它将用邮件发送ERROR（和更高级）的消息到站点管理员
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'include_html': True,
#         },
#         'default': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': 'logs/all.log',  # 日志输出文件位置
#             'maxBytes': 1024 * 1024 * 5,  # 文件大小
#             'backupCount': 5,  # 备份份数
#             'formatter': 'standard',  # 使用哪种formatters日志格式
#         },
#         'error': {
#             'level': 'ERROR',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': 'logs/error.log',  # 日志输出文件位置
#             'maxBytes': 1024 * 1024 * 5,  # 文件大小
#             'backupCount': 5,  # 备份份数
#             'formatter': 'standard',  # 这个handler 使用simple 输出格式。
#         },
#         'console': {  # 一个StreamHandler，它将打印DEBUG（和更高级）的消息到stderr。
#             'level': 'DEBUG',  # DEBUG：用于调试目的的底层系统信息
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard'  # 这个handler 使用simple 输出格式。
#         },
#         'request_handler': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': 'logs/script.log',
#             'maxBytes': 1024 * 1024 * 5,
#             'backupCount': 5,
#             'formatter': 'standard',
#         },
#         'scprits_handler': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': 'logs/script.log',
#             'maxBytes': 1024 * 1024 * 5,
#             'backupCount': 5,
#             'formatter': 'standard',
#         }
#     },
#     'loggers': {
#         'django': {  # django将DEBUG级以上的内容交给default和console
#             'handlers': ['default', 'console'],
#             'level': 'DEBUG',
#             'propagate': False
#         },
#         'django.request': {  # django.request将DEBUG级别以上的内容交给request_handler
#             'handlers': ['request_handler'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#         'scripts': {  # scripts将INFO级别以上的内容交给scprits_handler
#             'handlers': ['scprits_handler'],
#             'level': 'INFO',
#             'propagate': False
#         },
#         'blog.views': {  # blog.views将DEBUG级别以上的内容交给default和error
#             'handlers': ['default', 'error'],
#             'level': 'DEBUG',
#             'propagate': True
#         },
#     }
# }
