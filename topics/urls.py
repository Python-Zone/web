# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.topic_list, name="topics.topic_list"),
    url(r'^add/$', views.topic_add, name="topics.topic_add"),
    url(r'^(?P<id_>\d+)/edit/$', views.topic_edit, name="topics.topic_edit"),
    url(r'^(?P<id_>\d+)/delete/$', views.topic_delete, name="topics.topic_delete"),
    url(r'^(?P<id_>\d+)/$', views.topic_detail, name="topics.topic_detail"),
    url(r'^(?P<topic_id>\d+)/reply/add/$', views.reply_add, name="topics.reply_add"),

    url(r'^node(?P<id_>\d+)/$', views.node_list, name="topics.node_list"),


]
