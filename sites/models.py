# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.db import models


class Site(models.Model):
    CHINA_BUSINESS_SITE = 10
    CHINA_STARTUP_SITE = 20
    FOREIGN_FAMOUS_SITE = 30
    FAMOUS_BLOG_SITE = 40
    PYTHON_COMMUNITY = 50
    KIND_CHOICES = (
        (CHINA_BUSINESS_SITE, "国内商业网站"),
        (CHINA_STARTUP_SITE, "国内创业公司"),
        (FOREIGN_FAMOUS_SITE, "国外企业/团队"),
        (FAMOUS_BLOG_SITE, "技术博客"),
        (PYTHON_COMMUNITY, "Python社区"),
    )
    kind = models.IntegerField(null=True, choices=KIND_CHOICES, verbose_name="类型")
    name = models.CharField(max_length=100, verbose_name='名称')
    url = models.CharField(max_length=500, verbose_name='公司主页')
    abstract = models.TextField(default='', verbose_name='公司简介')
    weight = models.IntegerField(default=0, verbose_name='排名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "酷站"


