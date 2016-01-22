# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'yijingping'
import requests
from lxml import etree
from io import StringIO
from hashlib import md5
from datetime import datetime
from .models import Topic
from django.utils.encoding import smart_str

HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
}


def encode_dict(data):
    for k,v in data.iteritems():
        #print k, ":", v
        data[k] = smart_str(v)

class TopicCrawler(object):

    def get_lists(self):
        api = 'http://python.jobbole.com/all-posts/page/%d/'
        lists = []
        for item in range(1, 3):
            lists.append({
                "url": api % item,
                "method": "get"
            })
        return lists

    def get_item_from_list(self, lists):
        for l in lists:
            list_rsp = requests.get(l["url"], headers=HEADER)
            html = list_rsp.text
            htmlparser = etree.HTMLParser()
            tree = etree.parse(StringIO(html), htmlparser)

            nodes = tree.xpath("//div[@class='post floated-thumb']")
            for node in nodes:
                url = node.find(".//span[@class='read-more']/a[@href]").attrib['href']
                print "##list_url:%s, url: %s" % (l['url'], url)
                originid = url.split('/')[-2]
                avatar = node.find(".//div[@class='post-thumb']/a/img[@src]")
                avatar = avatar.attrib['src'] if avatar is not None else ''
                publish_time = self._process_datetime([x for x in node.find(".//div[@class='post-meta']/p").itertext()][2].strip()[:-1].strip())
                data = {
                    'kind': 2,
                    'uniqueid': self._calc_uniqueid(url),
                    'url': url,
                    'avatar': avatar,
                    'title': node.find(".//a[@class='archive-title']").text,
                    'user_id': 1,
                    'content': '',
                    'publish_time': publish_time
                }
                encode_dict(data)
                topic = Topic.objects.update_or_create(uniqueid=data["uniqueid"], defaults=data)

    def _calc_uniqueid(self, url):
        return md5(url).hexdigest()


    def _process_datetime(self, dtstr):
        today = datetime.now()
        try:
            res = datetime.strptime(dtstr, '%Y/%m/%d')
        except ValueError:
            res = today

        return res

    def run(self):
        # self.process_item({
        #     "url": "http://www.lagou.com/jobs/1339691.html",
        #     "originid": "1339691"
        # })
        # return
        lists = self.get_lists()
        self.get_item_from_list(lists)


if __name__ == '__main__':
    crawler = TopicCrawler()
    crawler.run()
