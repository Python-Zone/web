# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.db import models


class Job(models.Model):
    uniqueid = models.CharField(unique=True, max_length=100, verbose_name='url的md5值')
    url = models.CharField(max_length=500, verbose_name='文章的url')
    avatar = models.CharField(max_length=500, verbose_name='缩略图地址')
    title = models.CharField(max_length=200, verbose_name='标题')
    description = models.TextField(verbose_name='职位描述')
    salary_min = models.IntegerField(default=0, verbose_name='最低薪资')
    salary_max = models.IntegerField(default=0, verbose_name='最高薪资')
    city = models.CharField(default='', max_length=50, verbose_name='城市')
    address = models.CharField(default='', max_length=200, verbose_name='工作地点')
    company = models.CharField(default='', max_length=50, verbose_name='公司名称')
    company_site = models.CharField(default='', max_length=50, verbose_name='公司主页')
    company_stage = models.CharField(default='', max_length=50, verbose_name='公司阶段')
    industry_area = models.CharField(default='', max_length=100, verbose_name='行业领域')
    publish_time = models.DateTimeField(verbose_name='发布时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='抓取时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "职位"




