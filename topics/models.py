# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.db import models


class Topic(models.Model):
    uniqueid = models.CharField(unique=True, max_length=100, verbose_name='url的md5值')
    url = models.CharField(max_length=500, verbose_name='文章的url')
    site = models.CharField(max_length=200, verbose_name='来源网站')
    originid = models.CharField(max_length=200, verbose_name='来源id')
    avatar = models.CharField(max_length=500, verbose_name='缩略图地址')
    title = models.CharField(max_length=200, verbose_name='标题')
    author = models.CharField(max_length=50, verbose_name='作者')
    abstract = models.TextField(default='', verbose_name='文章简介')
    content = models.TextField(default='', verbose_name='文章内容')
    tags = models.CharField(default='', max_length=50, verbose_name='文章标签,以|分割')
    publish_time = models.DateTimeField(verbose_name='发布时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='抓取时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "文章"