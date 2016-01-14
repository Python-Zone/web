# -*- coding: utf-8 -*-
__author__ = 'yijingping'
import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from topics.models import Topic, Reply
from .models import Follow, Notification
from socketIO_client import SocketIO, BaseNamespace


class SocketIOHandler(object):
    def __init__(self):
        self.client = None

    def error_handler(self):
        self.client = None

    def get_client(self):
        if self.client:
            pass
        else:
            self.client = SocketIO(settings.WEBSOCKET_HOST, settings.WEBSOCKET_PORT, BaseNamespace)
            self.client.on_error(self.error_handler)
            self.wait(20)
        return self.client


siohandler = SocketIOHandler()

@receiver(post_save, sender=Topic)
def topic_add_notifications(sender, instance, created, **kwargs):
    if created:
        for follow in instance.user.followers.all():
            Notification.objects.create(kind=Notification.KIND_TOPIC_ADD, user=follow.from_user, content=json.dumps({
                "topic_id": instance.id
            }))


@receiver(post_save, sender=Reply)
def reply_add_notifications(sender, instance, created, **kwargs):
    if created:
        for follow in instance.user.followers.all():
            Notification.objects.create(kind=Notification.KIND_REPLY_ADD, user=follow.from_user, content=json.dumps({
                "reply_id": instance.id
            }))


@receiver(post_save, sender=Follow)
def follow_add_notifications(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(kind=Notification.KIND_FOLLOW_ME, user=instance.to_user, content=json.dumps({
            "follow_id": instance.id
        }))


@receiver(post_save, sender=Notification)
def notification_add(sender, instance, created, **kwargs):
    if created:
        client = siohandler.get_client()
        if client:
            client.emit('send notification', instance.user.id)