# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.shortcuts import render_to_response
from qiniu import Auth
from django.conf import settings

from django.http import JsonResponse
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from topics.models import Topic, Section


def index(request):
    params = request.GET.copy()
    _obj_list = Topic.objects.filter(status=Topic.STATUS_SHOW).order_by('-publish_time')

    paginator = Paginator(_obj_list, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        topics = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        topics = paginator.page(paginator.num_pages)

    return render_to_response('topics/topic_list.html', RequestContext(request, {
        "topics": topics,
        "active_nav": "topics",
        "sections": Section.objects.order_by('-weight'),
        "params": params,
        "from_node": ""
    }))


QINIU_AUTH = Auth(settings.QINIU_CONFIG["ACCESS_KEY"], settings.QINIU_CONFIG["SECRET_KEY"])


def qiniu_uptoken(request):
    token = QINIU_AUTH.upload_token(bucket=settings.QINIU_CONFIG["BUCKET"])
    return JsonResponse({"uptoken": token})