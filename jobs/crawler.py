# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'yijingping'
import requests
from lxml import etree
from io import StringIO
from hashlib import md5
from datetime import datetime
from .models import Job
from django.utils.encoding import smart_str


def print_dict(data):
    for k,v in data.iteritems():
        print k, ":", v
        data[k] = smart_str(v)

class JobCrawler(object):

    def get_lists(self):
        api = 'http://www.lagou.com/jobs/positionAjax.json?px=new'
        lists = []
        for item in range(0, 90):
            lists.append({
                "url": api,
                "method": "post",
                "payload": {"first": "false", "pn": item, "kd": "python"}
            })
        return lists

    def get_item_from_list(self, lists):
        items = []
        for l in lists:
            list_rsp = requests.post(l["url"],data=l["payload"])
            result = list_rsp.json()["content"]["result"]
            for item in result:
                items.append({
                    "url": "http://www.lagou.com/jobs/%s.html" % item["positionId"],
                    "method": "get"
                })

        return items

    def _calc_uniqueid(self, url):
        return md5(url).hexdigest()

    def _process_salary(self, salary):
        data = salary.split('-')
        if len(data) == 2:
            salary_min = int(data[0][:-1]) * 1000
            salary_max = int(data[1][:-1]) * 1000
        elif salary[-2:] == "以上":
            salary_min = int(salary[:-3]) * 1000
            salary_max = 0
        elif salary[-2:] == "以下":
            salary_min = 0
            salary_max = int(salary[:-3]) * 1000
        else:
            salary_min, salary_max = 0, 0

        return (salary_min, salary_max)

    def _process_datetime(self, dtstr):
        today = datetime.now()
        try:
            res = datetime.strptime(dtstr, '%Y-%m-%d')
        except ValueError:
            try:
                res = datetime.strptime(dtstr, '%Y-%m-%d')
                res = res.replace(year=today.year, month=today.month, day=today.day)
            except ValueError:
                res = today

        return res

    def _fill_blank(self, data, idx):
        if len(data) > idx:
            return data[idx]
        else:
            return ''

    def process_item(self, item):
        url = item["url"]
        print "url:", url
        rsp = requests.get(url)
        html = rsp.text
        htmlparser = etree.HTMLParser()
        tree = etree.parse(StringIO(html), htmlparser)

        salary_min, salary_max = self._process_salary(tree.xpath(
                "/html/body/div[@id='container']/div[@class='content_l fl']/dl[@class='job_detail']/dd[@class='job_request']/p[1]/span[@class='red']/text()"
        )[0])
        publish_time = self._process_datetime(tree.xpath(
                "//dl[@class='job_detail']/dd[@class='job_request']/p[@class='publish_time']/text()"
        )[0].split()[0])
        data = {
            "uniqueid": self._calc_uniqueid(url),
            "url": url,
            "site": "拉勾网",
            "title": tree.xpath("//dl[@class='job_detail']/dt[@class='clearfix join_tc_icon']/h1/text()")[2].strip(),
            "salary_min": salary_min,
            "salary_max": salary_max,
            "city": tree.xpath("//dl[@class='job_detail']/dd[@class='job_request']/p[1]/span[2]/text()")[0],
            "experience": tree.xpath("//dl[@class='job_detail']/dd[@class='job_request']/p[1]/span[3]/text()")[0],
            "education": tree.xpath("//dl[@class='job_detail']/dd[@class='job_request']/p[1]/span[4]/text()")[0],
            "worktype": tree.xpath("//dl[@class='job_detail']/dd[@class='job_request']/p[1]/span[5]/text()")[0],

            "address": tree.xpath("//dl[@class='job_company']/dd/div[1]/text()")[0].strip(),
            "company": tree.xpath("//dl[@class='job_company']/dt/a/div/h2[@class='fl']/text()")[0].strip(),
            "company_shortname":"",
            "company_site": self._fill_blank(tree.xpath("//dl[@class='job_company']/dd/ul[@class='c_feature'][1]/li[3]/a/text()"), 0),
            "company_stage": tree.xpath("//dl[@class='job_company']/dd/ul[@class='c_feature'][2]/li/text()")[0].strip(),
            "industry_area": tree.xpath("//dl[@class='job_company']/dd/ul[@class='c_feature'][1]/li[1]/text()")[1].strip(),
            "publish_time": publish_time
        }
        print_dict(data)

        job = Job.objects.update_or_create(uniqueid=data["uniqueid"], defaults=data)


    def run(self):
        # self.process_item({
        #     "url": "http://www.lagou.com/jobs/1339691.html"
        # })
        # return
        lists = self.get_lists()
        items = self.get_item_from_list(lists)
        for item in items:
            self.process_item(item)


if __name__ == '__main__':
    crawler = JobCrawler()
    crawler.run()
