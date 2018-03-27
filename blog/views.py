from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from django.db.models import Q  # filter(~Q(name=''))过滤表示不等于
from .models import Category, Tag, Article, Comment, Links


# Create your views here.
# 定义全局变量函数，将函数中的变量通过locals()返回
# 将global_setting函数加到 settings.py/TEMPLATES/OPTIONS 的上下文处理器中
def global_setting(request):
    tags = Tag.objects.all()
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

    return locals()

# 首页视图
def index(request):
    articles = Article.objects.all()

    return render(request, 'blog/index.html', locals())

# 文章内容视图
def article_detail(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/article.html', locals())

# 文章列表视图
def article_list(request, category_id, page=1):
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
