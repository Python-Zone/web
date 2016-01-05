# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from captcha.models import CaptchaStore, get_safe_now


def check_captcha(key, value):
    CaptchaStore.remove_expired()
    try:
        CaptchaStore.objects.get(hashkey=key, response=value, expiration__gt=get_safe_now()).delete()
    except CaptchaStore.DoesNotExist:
        return False

    return True