# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'yijingping'
from django.core.management.base import BaseCommand, CommandError
from topics.crawler import TopicCrawler

class Command(BaseCommand):
    help = '抓取伯乐在线python下的所有文章'

    def handle(self, *args, **options):
        crawler = TopicCrawler()
        crawler.run()
