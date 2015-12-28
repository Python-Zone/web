# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'yijingping'
from django.core.management.base import BaseCommand, CommandError
from jobs.crawler import JobCrawler

class Command(BaseCommand):
    help = '抓取拉勾网的python职位'

    def handle(self, *args, **options):
        crawler = JobCrawler()
        crawler.run()
