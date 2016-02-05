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
        return dt.strftime("%H:%M")
    elif seconds <= 60 * 60 * 24 * 3:
        return "%d天前 %s" % (int(seconds / (60 * 60 * 24)), dt.strftime("%H:%M"))
    else:
        return dt.strftime("%Y-%m-%d %H:%M")