# -*- coding: utf-8 -*-
import json
from wechat_sdk import WechatBasic
from web.settings import WEIXIN
from .models import Config


def get_access_token():
    try:
        res = Config.objects.get(type=Config.TYPE_TOKEN)
    except Config.DoesNotExist:
        return None, None
    else:
        print res.value
        value = json.loads(res.value)
        return value.get("access_token"), value.get("access_token_expires_at")


def set_access_token(access_token, access_token_expires_at):
    value = json.dumps({
        "access_token": access_token,
        "access_token_expires_at": access_token_expires_at
    })

    obj, created = Config.objects.update_or_create(
        type=Config.TYPE_TOKEN,
        defaults={
            "value": value
        }
    )


def get_jsapi_ticket():
    try:
        res = Config.objects.get(type=Config.TYPE_TICKET)
    except Config.DoesNotExist:
        return None, None
    else:
        value = json.loads(res.value)
        return value.get("jsapi_ticket"), value.get("jsapi_ticket_expires_at")


def set_jsapi_ticket(jsapi_ticket, jsapi_ticket_expires_at):
    value = json.dumps({
        "jsapi_ticket": jsapi_ticket,
        "jsapi_ticket_expires_at": jsapi_ticket_expires_at
    })

    obj, created = Config.objects.update_or_create(
        type=Config.TYPE_TICKET,
        defaults={
            "value": value
        }
    )


wechat = WechatBasic(
    token=WEIXIN["WEIXIN_TOKEN"],
    appid=WEIXIN["WEIXIN_APP_ID"],
    appsecret=WEIXIN["WEIXIN_APP_SECRET"],
    get_access_token=get_access_token,
    set_access_token=set_access_token,
    get_jsapi_ticket=get_jsapi_ticket,
    set_jsapi_ticket=set_jsapi_ticket
)
