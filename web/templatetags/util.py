# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django import template
from datetime import datetime, timedelta
register = template.Library()


@register.filter
def update_city(params, city):
    res = params or {}
    res['city'] = city
    return res


@register.filter
def readable_datetime(dt):
    delta = datetime.now() - dt
    seconds = delta.total_seconds()
    if seconds <= 60:
        return "1分钟内"
    elif seconds <= 60 * 60:
        return "%d分钟前" % int(seconds / 60)
    elif seconds <= 60 * 60 * 24:
        return "%d小时前" % int(seconds / (60 * 60))
    elif seconds <= 60 * 60 * 24 * 3:
        return "%d天前" % int(seconds / (60 * 60 * 24))
    else:
        return dt.strftime("%Y-%m-%d")