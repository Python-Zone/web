# -*- coding: utf-8 -*-
__author__ = 'yijingping'
import time
from django.db import models


def get_default_uniqueid():
    return str(long(time.time() * 1000000))


class Topic(models.Model):
    STATUS_SHOW = 1
    STATUS_DELETE = 2
    STATUS_CHOICES = (
        (STATUS_SHOW, '显示'),
        (STATUS_DELETE, '删除')
    )
    # 抓取文章所需关键字
    uniqueid = models.CharField(unique=True, max_length=100, default=get_default_uniqueid, verbose_name='url的md5值')
    url = models.CharField(max_length=500, default='', verbose_name='文章的url')
    site = models.CharField(max_length=200, default='', verbose_name='来源网站')
    originid = models.CharField(max_length=200, default='', verbose_name='来源id')
    avatar = models.CharField(max_length=500, default='', verbose_name='缩略图地址')
    author = models.CharField(max_length=50, default='', verbose_name='作者')
    abstract = models.TextField(default='', verbose_name='文章简介')

    # 发布的文章需要的信息
    title = models.CharField(max_length=200, verbose_name='标题')
    node = models.ForeignKey('Node', default=8, verbose_name='所属节点') # 默认是8 文章节点
    user = models.ForeignKey('users.User', null=True, related_name='topics', verbose_name='作者')
    content = models.TextField(default='', verbose_name='文章内容')
    source = models.TextField(default='', verbose_name='markdown原格式')
    tags = models.CharField(default='', max_length=50, verbose_name='文章标签,以|分割')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    status = models.IntegerField(default=STATUS_SHOW, choices=STATUS_CHOICES, verbose_name="是否显示")

    # 回复条数
    replies_count = models.IntegerField(default=0, verbose_name='回复条数')
    last_reply_user = models.ForeignKey('users.User', null=True, related_name='my_replied_topics', verbose_name='最后回复人')
    reply_time = models.DateTimeField(null=True, verbose_name='最后回复时间')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "文章"


class Reply(models.Model):
    STATUS_SHOW = 1
    STATUS_DELETE = 2
    STATUS_CHOICES = (
        (STATUS_SHOW, '显示'),
        (STATUS_DELETE, '删除')
    )
    topic = models.ForeignKey('Topic', related_name="replies", verbose_name='回复的文章')
    user = models.ForeignKey('users.User', related_name='replies', verbose_name='回复人')
    content = models.TextField(default='', verbose_name='文章内容')
    source = models.TextField(default='', verbose_name='markdown原格式')
    status = models.IntegerField(default=1, verbose_name="是否显示")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name_plural = "回复"


class Section(models.Model):
    name = models.CharField(max_length=50, verbose_name='分区名称')
    weight = models.IntegerField(default=0, verbose_name='权重')

    @property
    def nodes(self):
        return Node.objects.filter(section=self).order_by('-weight')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "分区"


class Node(models.Model):
    section = models.ForeignKey('Section', verbose_name='所属分区')
    name = models.CharField(max_length=50, verbose_name='节点名称')
    desc = models.TextField(default='', verbose_name='节点描述')
    weight = models.IntegerField(default=0, verbose_name='权重')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "节点"