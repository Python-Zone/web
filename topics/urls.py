# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.topic_list, name="topics.topic_list"),
    url(r'^\d+/$', views.topic, name="topics.topic"),

    url(r'^node(?P<id_>\d+)/$', views.node_list, name="topics.node_list"),


]
