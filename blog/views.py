from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from django.db.models import Q  # filter(~Q(name=''))过滤表示不等于
from .models import Category, Tag, Article, Comment, Links
from .cache_manager import update_article_hits
from .cache_manager.cache_sync import syn_article_hits
from django.views.decorators.cache import cache_page


# Create your views here.
# 定义全局变量函数，将函数中的变量通过locals()返回
# 将global_setting函数加到 settings.py/TEMPLATES/OPTIONS 的上下文处理器中
def global_setting(request):
    tags = Tag.objects.filter(is_display=1).all()
    links = Links.objects.all()

    # 图文推荐文章列表对象
    recommend_articles = Article.objects.filter(~Q(picture='')).filter(is_recommend=1).order_by('-hits')[:5]

    # 点击排行版文章列表对象
    hits_articles = Article.objects.order_by('-hits')[:10]

    # 定义导航分类
    # 从数据库获取指定ID的分类对象列表（置于技术杂谈导航下）
    nav_jszt_category = Category.objects.filter(id__in=settings.NAV_JSZT_CATEGORY).order_by('-index')

    # 从数据库获取指定ID的分类对象列表（置于生活随笔导航下）
    nav_shsb_category = Category.objects.filter(id__in=settings.NAV_SHSB_CATEGORY).order_by('-index')

    # settings中站点基本信息配置
    site_name = settings.SITE_NAME
    site_keywords = settings.SITE_KEYWORDS
    site_desc = settings.SITE_DESC
    site_beian = settings.SITE_BEIAN

    pro_mail = settings.PRO_EMAIL

    return locals()

# 首页视图
# 对当前视图的输出进行缓存，时间15分钟（推荐在conf中指定视图缓存）
# @cache_page(60*15)
def index(request):
    articles = Article.objects.all()

    return render(request, 'blog/index.html', locals())

# 文章内容视图
def article_detail(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    # 更新文章点击次数
    update_article_hits(article)
    return render(request, 'blog/article.html', locals())

# 文章列表视图
def article_list(request, category_id, page=1):
    # 同步缓存和数据库中的文章点击次数
    syn_article_hits()
    # 分页，每页显示记录数
    per_page = settings.PER_PAGE

    category = get_object_or_404(Category, id=category_id)

    articles_list = Article.objects.filter(category_id=category_id)

    paginator = Paginator(articles_list, per_page)
    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
    articles = current_page.object_list

    return render(request, 'blog/article_list.html', locals())

# 标签页视图
def tag_article_list(request, id, page=1):
    per_page = settings.PER_PAGE

    tag = get_object_or_404(Tag, id=id)

    articles_list = tag.article.all()

    paginator = Paginator(articles_list, per_page)
    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
    articles = current_page.object_list

    return render(request, 'blog/tag_article_list.html', locals())
