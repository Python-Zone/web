# -*- coding: utf-8 -*-
__author__ = 'yijingping'
import time
from django.db import models


def get_default_uniqueid():
    return str(long(time.time() * 1000000))


class Topic(models.Model):
    KIND_TOPIC = 1
    KIND_URL = 2
    KIND_TOPIC_WITH_URL = 3
    KIND_CHOICES = (
        (KIND_TOPIC, '文章,不显示原文链接'),
        (KIND_URL, 'URL'),
        (KIND_TOPIC_WITH_URL, '文章,显示原文链接'),
    )
    STATUS_SHOW = 1
    STATUS_DELETE = 2
    STATUS_CHOICES = (
        (STATUS_SHOW, '显示'),
        (STATUS_DELETE, '删除')
    )
    kind = models.IntegerField(default=KIND_TOPIC, choices=KIND_CHOICES, verbose_name="通知类型")
    # 抓取文章所需关键字
    uniqueid = models.CharField(unique=True, max_length=100, default=get_default_uniqueid, verbose_name='url的md5值')
    url = models.CharField(max_length=500, default='', verbose_name='文章的url')
    avatar = models.CharField(max_length=500, default='', verbose_name='缩略图地址')

    # 发布的文章需要的信息
    title = models.CharField(max_length=200, verbose_name='标题')
    node = models.ForeignKey('Node', default=8, verbose_name='所属节点') # 默认是8 文章节点
    user = models.ForeignKey('users.User', null=True, related_name='topics', verbose_name='作者')
    content = models.TextField(default='', verbose_name='文章内容')
    source = models.TextField(default='', verbose_name='markdown原格式')
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
        index_together = [
            ["status", "publish_time"],
            ["publish_time"],
        ]


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


class Favorite(models.Model):
    STATUS_SHOW = 1
    STATUS_DELETE = 2
    STATUS_CHOICES = (
        (STATUS_SHOW, '显示'),
        (STATUS_DELETE, '删除')
    )
    user = models.ForeignKey('users.User', related_name='favorites', verbose_name='收藏者')
    topic = models.ForeignKey('topics.Topic', related_name='favorites', verbose_name='帖子')
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=STATUS_SHOW, verbose_name="是否显示")

    @staticmethod
    def is_favorite(user, topic):
        try:
            Favorite.objects.get(user=user, topic=topic, status=Favorite.STATUS_SHOW)
        except Favorite.DoesNotExist:
            return False
        else:
            return True


    class Meta:
        verbose_name_plural = "收藏"
        unique_together = ("user", "topic")
