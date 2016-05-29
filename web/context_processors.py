# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from users.models import User
from topics.models import Topic, Reply
from django.conf import settings

def global_stats(request):
    return {
        "GLOBAL_TOTAL_USER": User.objects.all().count() + 13655,
        "GLOBAL_TOTAL_TOPIC": Topic.objects.all().count(),
        "GLOBAL_TOTAL_REPLY": Reply.objects.all().count() + 27633,
        "WEBSOCKET_ENABLE": settings.WEBSOCKET_ENABLE,
        "WEBSOCKET_HOST": settings.WEBSOCKET_HOST,
        "WEBSOCKET_PORT": settings.WEBSOCKET_PORT,
        "BAIDU_AK": settings.BAIDU_AK
    }
