# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.wiki_list, name="wiki.wiki_list"),
    url(r'^\d+/$', views.wiki, name="wiki.wiki"),

]
