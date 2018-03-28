# -*- encoding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.core.cache import cache
from django_redis import get_redis_connection
# from django.conf import settings
# import datetime

# # 获取redis配置的当前db
# current_db = settings.CACHES['default']['LOCATION'].rsplit('/', 1)[1]

# 获取redis客户端操作对象
rds = get_redis_connection('default')

def update_article_hits(article):
    """更新文章点击次数"""
    # 指定key不存在则从数据库hits字段添加，并设置永不过期
    cache.add("article:{}:views".format(article.id), article.hits, timeout=None)

    # 指定key的值自增1
    cache.incr("article:{}:views".format(article.id))

def get__article_hits(article):
    """获取文章点击次数"""
    # 指定key不存在则从数据库hits字段添加，并设置永不过期
    cache.add("article:{}:views".format(article.id), article.hits, timeout=None)

    return cache.get("article:{}:views".format(article.id))
#
# def syn_article_hits():
#     """将redis缓存中的点击次数同步到数据库中"""
#     for key in cache.keys("article:*:views"):
#         # 从key中获取文章id值
#         article_id = int(key.split(':')[1])
#         try:
#             article = get_object_or_404(Article, id=article_id)
#             # 如果数据库中的点击次数大于缓存的值，则更新缓存中的值，否则将缓存中的值存入数据库中
#             if article.hits > int(cache.get(key)):
#                 cache.set(key, article.hits)
#             else:
#                 article.hits = int(cache.get(key))
#                 article.save()
#         except:
#             # 数据库中已不存在该文章则redis删除该键
#             cache.delete(key)

# def get_hits_sorts(date_end, days, item_num, article):
#     """获取指定时间段内的点击排行榜记录条数"""
#     date_start = date_end - datetime.timedelta(days)

