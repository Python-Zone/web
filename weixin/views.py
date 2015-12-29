# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'yijingping'
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .util import wechat
from wechat_sdk.messages import TextMessage, EventMessage

@csrf_exempt
def index(request):
    if request.method == 'GET':
        # 处理微信的echostr验证消息
        echostr = request.GET.get('echostr')
        signature = request.get('signature')
        timestamp = request.get('timestamp')
        nonce = request.get('nonce')

        if wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponse(echostr)
        else:
            print "check signature failed"
            return HttpResponse("check signature failed")
        pass
    elif request.method == 'POST':
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce', None)
        body_text = request.body

        if wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
            # 对 XML 数据进行解析 (必要, 否则不可执行 response_text, response_image 等操作)
            wechat.parse_data(body_text)
            # 获得解析结果, message 为 WechatMessage 对象 (wechat_sdk.messages中定义)
            message = wechat.get_message()

            response = None
            if isinstance(message, TextMessage):
                response = wechat.response_news([
                    {
                        'title': '欢迎关注Python社区',
                        'description': '我们将每天为你推送Python最新的文章、职位、公司和教学信息。',
                        'picurl': 'http://7teb7o.com1.z0.glb.clouddn.com/activity/b0.jpg',
                        'url': 'http://pythonzone.bowenpay.com/jobs/job/'
                    },
                ])
            elif isinstance(message, EventMessage):  # 事件信息
                if message.type == 'subscribe':  # 关注事件(包括普通关注事件和扫描二维码造成的关注事件)
                    response = wechat.response_news([
                        {
                            'title': '欢迎关注Python社区',
                            'description': '我们将每天为你推送Python最新的文章、职位、公司和教学信息。',
                            'picurl': 'http://7teb7o.com1.z0.glb.clouddn.com/activity/b0.jpg',
                            'url': 'http://pythonzone.bowenpay.com/jobs/job/'
                        },
                    ])
                elif message.type == 'click':
                    if message.key == 'Jobs':
                        response = wechat.response_news([
                            {
                                'title': '为你推荐的职位信息',
                                'description': '每天自动更新最新的Python职位,不放过任何一个好的工作机会.',
                                'picurl': 'http://7teb7o.com1.z0.glb.clouddn.com/activity/b0.jpg',
                                'url': 'http://pythonzone.bowenpay.com/jobs/job/'
                            },
                        ])

            return HttpResponse(response or '')
