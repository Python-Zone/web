# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^community/$', views.community_list, name="data.community_list"),
    url(r'^community/heatdata/$', views.community_heat_data, name="data.community_heat_data"),

]
