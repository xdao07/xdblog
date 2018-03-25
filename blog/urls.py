from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^home/$', TemplateView.as_view(template_name='blog/index.html'), name='home'),
    url(r'^technology-list/$', TemplateView.as_view(template_name='blog/technology_list.html'), name='technology_list'),
    url(r'^dailylife-list/$', TemplateView.as_view(template_name='blog/dailylife_list.html'), name='dailylife_list'),
    url(r'^aboutme/$', TemplateView.as_view(template_name='blog/aboutme.html'), name='aboutme'),
    url(r'^messageme/$', TemplateView.as_view(template_name='blog/messageme.html'), name='messageme'),
    url(r'^article-list/$', TemplateView.as_view(template_name='blog/article_list.html'), name='article_list'),
    url(r'^article/$', TemplateView.as_view(template_name='blog/article.html'), name='article'),
]
