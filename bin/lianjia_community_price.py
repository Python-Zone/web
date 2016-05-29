# -*- coding: utf-8 -*-
__author__ = 'yijingping'
# 加载django环境
import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'web.settings'
import django
django.setup()

import logging
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

import json
import requests
from django.conf import settings
from django.db.models import Q
from data.models import Community

class CommunityPrice(object):
    """ 小区房价 """
    def run(self):
        communities = Community.objects.filter(Q(sell_trend__isnull=True) | Q(price_trend__isnull=True))
        print communities.count()
        for comm in communities:
            cid = comm.url.split('/')[-2]
            url = 'http://bj.lianjia.com/fangjia/priceTrend/c%s' % cid
            try:
                r = requests.get(url).json()
                comm.price_trend = json.dumps(r['currentLevel']['dealPrice']['total'])
                comm.sell_trend = json.dumps(r['currentLevel']['quantity']['total'])
                comm.save()
            except Exception as e:
                logging.exception(e)


if __name__ == '__main__':
    communityPrice = CommunityPrice()
    communityPrice.run()