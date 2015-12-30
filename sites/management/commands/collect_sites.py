# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'yijingping'
from django.db.models import Count
from django.core.management.base import BaseCommand
from jobs.models import Job
from sites.models import Site

SITES = ['阿里巴巴', '美团', '腾讯', '百度', '爱奇艺', '蓝汛', '百分点', '饿了么', '中软国际' , '今日头条', '360',
         '龙图', '创新工场', '知乎', '乐视', '携程', '暴风影音', '优酷', '土豆', '金山', '掌阅', '绿盟', '宜信公司',
         '唯品会', '多盟', '果壳', '点乐', '京东', '中软', '豆瓣']

class Command(BaseCommand):
    help = '从jobs中获取sites'

    def is_business_site(self, name):
        try:
            site = Site.objects.get(name=name)
        except Site.DoesNotExist:
            pass
        else:
            if site.kind == Site.CHINA_BUSINESS_SITE:
                return site.kind

        global SITES
        return any(map(lambda x: x in name, SITES))


    def handle(self, *args, **options):
        jobs = Job.objects.values_list('company', 'company_site').annotate(
                weight=Count('company')).distinct().order_by('-weight')
        for item in jobs:
            kind = Site.CHINA_BUSINESS_SITE if self.is_business_site(item[0]) else Site.CHINA_STARTUP_SITE

            Site.objects.update_or_create(name=item[0], defaults={
                'kind': kind,
                'name': item[0],
                'url': item[1],
                'weight': item[2] * 100
            })
