# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django import template

register = template.Library()


@register.filter
def update_city(params, city):
    res = params or {}
    res['city'] = city
    return res