# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import JsonResponse
from qiniu import Auth
from django.conf import settings

def index(request):
    return render_to_response('index.html', RequestContext(request, {}))



QINIU_AUTH = Auth(settings.QINIU_CONFIG["ACCESS_KEY"], settings.QINIU_CONFIG["SECRET_KEY"])


def qiniu_uptoken(request):
    token = QINIU_AUTH.upload_token(bucket=settings.QINIU_CONFIG["BUCKET"])
    return JsonResponse({"uptoken": token})