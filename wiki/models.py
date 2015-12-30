# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.db import models


class Wiki(models.Model):
    PRIMARY_GRADE = 10
    ADVANCED_GRADE = 20
    WEB_DEVELOPMENT = 30
    SYSTEM_DEVELOPMENT = 40
    BIG_DATA_DEVELOPMENT = 50
    QUANT_DEVELOPMENT = 60
    KIND_CHOICES = (
        (PRIMARY_GRADE, "Python 入门教程"),
        (ADVANCED_GRADE, "Python 高级进阶教程"),
        (WEB_DEVELOPMENT, "Web开发"),
        (SYSTEM_DEVELOPMENT, "系统管理"),
        (BIG_DATA_DEVELOPMENT, "云计算/大数据/机器学习"),
        (QUANT_DEVELOPMENT, "量化分析"),
    )
    STATUS_DEFAULT = 0
    STATUS_DISABLE = 1
    STATUS_DELETE = 2
    STATUS_CHOICES = (
        (STATUS_DEFAULT, '已发布'),
        (STATUS_DISABLE, '未发布'),
        (STATUS_DELETE, '已删除')
    )
    kind = models.IntegerField(null=True, choices=KIND_CHOICES, verbose_name="类型")
    title = models.CharField(max_length=100, verbose_name='标题')
    subhead = models.CharField(default='', blank=True, max_length=100, verbose_name='副标题')
    url = models.CharField(default='', blank=True, max_length=500, verbose_name='外链')
    author = models.CharField(max_length=50, verbose_name='作者')
    content = models.TextField(default='', blank=True, verbose_name='文章内容')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    weight = models.IntegerField(default=0, verbose_name='排名')
    status = models.IntegerField(default=STATUS_DEFAULT, choices=STATUS_CHOICES, verbose_name="状态")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "wiki"


