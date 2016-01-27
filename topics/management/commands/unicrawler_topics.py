# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'yijingping'
import redis
import json
from django.conf import settings
from hashlib import md5
from django.core.management.base import BaseCommand, CommandError
from topics.models import Topic
from django.utils.encoding import smart_str


def encode_dict(data):
    for k,v in data.iteritems():
        #print k, ":", v
        if isinstance(v, basestring):
            data[k] = smart_str(v)


def get_uniqueid(url):
    return md5(url).hexdigest()


class Command(BaseCommand):
    help = '抓取伯乐在线python下的所有文章'

    def handle(self, *args, **options):
        r = redis.StrictRedis(**settings.REDIS_CONFIG["unicrawler"])
        while True:
            try:
                resp = r.brpop('unicrawler:data:topics')
            except Exception as e:
                print e
                continue

            resp_data = json.loads(resp[1])
            print '--------------------------------------------------------------'
            url =  resp_data['url']
            data = {
                    'kind': Topic.KIND_URL,
                    'uniqueid': get_uniqueid(url),
                    'url': url,
                    'avatar': resp_data.get('avatar', ''),
                    'title': resp_data.get('title', ''),
                    'node_id': resp_data.get('node_id', None),
                    'user_id': resp_data.get('user_id', None),
                    'content': resp_data.get('content', ''),
                    'publish_time': resp_data.get('publish_time', '')
                }
            encode_dict(data)
            print json.dumps(data)
            topic = Topic.objects.update_or_create(uniqueid=data["uniqueid"], defaults=data)
