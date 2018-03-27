from django.contrib import admin
from .models import Category, Tag, Article, Comment, Links

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'index')
    search_fields = ('name',)
    list_editable = ('index',)
admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_display')
    list_filter = ('is_display',)
    list_editable = ('is_display',)
admin.site.register(Tag, TagAdmin)

class ArticleAdmin(admin.ModelAdmin):
    exclude = ('id', 'slug', 'publish')
    list_display = ('title', 'slug', 'hits', 'is_recommend', 'publish', 'category')
    filter_horizontal = ('tag',)
    list_editable = ('hits', 'is_recommend',)
    list_filter = ('category',)
    date_hierarchy = 'publish'

    # 将指定的静态素材应用于当前表单中
    class Media:
        css = {
            'all': ('/static/blog/js/kindeditor-4.1.11-zh-CN/themes/simple/simple.css',),
        }
        js = (
            '/static/blog/js/kindeditor-4.1.11-zh-CN/kindeditor-all-min.js',
            '/static/blog/js/kindeditor-4.1.11-zh-CN/config.js',
            '/static/blog/js/kindeditor-4.1.11-zh-CN/lang/zh-CN.js',
        )
admin.site.register(Article, ArticleAdmin)

admin.site.register(Comment)

class LinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'publish', 'index')
    list_editable = ('url', 'index')
admin.site.register(Links, LinksAdmin)
