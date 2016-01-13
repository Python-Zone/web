# -*- coding: utf-8 -*-
__author__ = 'yijingping'
import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from topics.models import Topic, Reply
from .models import Follow, Notification


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