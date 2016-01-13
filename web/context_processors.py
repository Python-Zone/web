# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from users.models import User
from topics.models import Topic, Reply


def global_stats(request):
    return {
        "GLOBAL_TOTAL_USER": User.objects.all().count(),
        "GLOBAL_TOTAL_TOPIC": Topic.objects.all().count(),
        "GLOBAL_TOTAL_REPLY": Reply.objects.all().count()
    }
