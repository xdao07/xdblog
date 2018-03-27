# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-26 04:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='文章标题')),
                ('slug', models.CharField(max_length=200, verbose_name='标题映射链接名')),
                ('abstract', models.TextField(max_length=400, verbose_name='文章摘要')),
                ('content', models.TextField(verbose_name='内容')),
                ('hits', models.IntegerField(default=0, verbose_name='点击次数')),
                ('is_recommend', models.BooleanField(default=False, verbose_name='是否推荐（默认否）')),
                ('publish', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
            options={
                'ordering': ['-publish'],
                'verbose_name_plural': '文章',
                'verbose_name': '文章',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='分类名称')),
                ('index', models.IntegerField(default=999, verbose_name='分类排序（从大到小）')),
            ],
            options={
                'ordering': ['index'],
                'verbose_name_plural': '文章分类',
                'verbose_name': '文章分类',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('username', models.CharField(blank=True, max_length=45, verbose_name='用户名')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='邮箱')),
                ('url', models.URLField(blank=True, verbose_name='网址')),
                ('publish', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('pid', models.IntegerField(verbose_name='父级ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blog.Article', verbose_name='文章')),
            ],
            options={
                'ordering': ['-publish'],
                'verbose_name_plural': '留言/评论',
                'verbose_name': '留言/评论',
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45, verbose_name='链接标题')),
                ('description', models.CharField(max_length=100, verbose_name='链接描述')),
                ('url', models.URLField(verbose_name='链接网址')),
                ('publish', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('index', models.IntegerField(default=999, verbose_name='排序（从大到小）')),
            ],
            options={
                'ordering': ['-publish'],
                'verbose_name_plural': '友情链接',
                'verbose_name': '友情链接',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='标签名')),
                ('is_display', models.BooleanField(default=True, verbose_name='是否显示（默认是）')),
            ],
            options={
                'verbose_name_plural': '标签',
                'verbose_name': '标签',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to='blog.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(related_name='article', to='blog.Tag', verbose_name='标签'),
        ),
    ]