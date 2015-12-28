# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'yijingping'
from django.http import HttpResponse
from .util import wechat


def index(request):
    if request.method == 'GET':
        # 处理微信的echostr验证消息
        echostr = request.GET['echostr']
        signature = request.GET['signature']
        timestamp = request.GET['timestamp']
        nonce = request.GET['nonce']

        if wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponse(echostr)
        else:
            print "check signature failed"
            return HttpResponse("check signature failed")
        pass
    elif request.method == 'POST':
        pass

    """
    def post(self):
        signature = self.get_argument('signature')
        timestamp = self.get_argument('timestamp')
        nonce = self.get_argument('nonce', None)
        body_text = self.request.body

        if wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
            # 对 XML 数据进行解析 (必要, 否则不可执行 response_text, response_image 等操作)
            wechat.parse_data(body_text)
            # 获得解析结果, message 为 WechatMessage 对象 (wechat_sdk.messages中定义)
            message = wechat.get_message()

            response = None
            if isinstance(message, TextMessage):
                response = ''
            elif isinstance(message, EventMessage):  # 事件信息
                if message.type == 'subscribe':  # 关注事件(包括普通关注事件和扫描二维码造成的关注事件)
                    response = wechat.response_news([
                        {
                            'title': '欢迎来到波纹',
                            'description': '真正自由的积分平台，消费无使用限制。',
                            'picurl': 'http://7teb7o.com1.z0.glb.clouddn.com/activity/b0.jpg',
                            'url': 'http://' + WXWEB_DOMAIN
                        },
                    ])
                    event_key = message.key
                    now = datetime.now()
                    if event_key and 'qrscene_' in event_key:
                        MScanUser.create({
                            "openid": message.source,
                            "scene_id": int(event_key[len('qrscene_'):]),
                            "create": now,
                            "update": now,
                            "status": STATUS_DEFAULT
                        })
                elif message.type == 'click':
                    if message.key == 'ABOUT':
                        response = wechat.response_text(content='波纹科技是一家致力于通过创新来创造价值的互联网公司，成立于2014年的北京。目前，我们正努力使用互联网技术，打破传统积分之间的壁垒，让用户获得的积分可以随时消费、转账、兑换，将传统积分从流通域小，浪费闲置严重的“鸡肋”变成有用，易用，好用的“鸡腿”。')
                    elif message.key == 'PLAY':
                        response = wechat.response_text(content='1. 积分获取：低价从波纹平台购买，或进行积分消费获得积分返利 \n 2. 积分消费：通过波纹平台，用积分直接支付 \n 3. 积分兑换：任意积分可以和余额兑换，余额也可以兑换成其它积分 \n 4. 积分转账：亲朋好友的积分汇至一处，小积分变成大积蓄')


            return self.write(response or '')
        """
