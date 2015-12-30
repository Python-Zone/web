# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.site_list, name="sites.site_list"),
    url(r'^\d+/$', views.site, name="sites.site"),

]
