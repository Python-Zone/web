# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager

class User(AbstractBaseUser):
    name = models.CharField(max_length=30, unique=True)
    #password = models.CharField(max_length=128)
    nickname = models.CharField(max_length=100)
    email = models.CharField(unique=True, null=True, max_length=100)
    avatar = models.CharField(default='', blank=True, null=True, max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    #last_login = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['nickname']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def is_superuser(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def my_following(self):
        return Follow.objects.filter(from_user=self, status=Follow.STATUS_SHOW)

    @property
    def my_followers(self):
        return Follow.objects.filter(to_user=self, status=Follow.STATUS_SHOW)

    @property
    def my_favorites(self):
        return Favorite.objects.filter(user=self, status=Favorite.STATUS_SHOW)

    @property
    def my_notifications(self):
        return Notification.objects.filter(user=self).exclude(status=Notification.STATUS_DELETE)

    class Meta:
        verbose_name_plural = "用户"


class Follow(models.Model):
    STATUS_SHOW = 1
    STATUS_DELETE = 2
    STATUS_CHOICES = (
        (STATUS_SHOW, '显示'),
        (STATUS_DELETE, '删除')
    )
    from_user = models.ForeignKey('User', related_name='following', verbose_name='正在关注')
    to_user = models.ForeignKey('User', related_name='followers', verbose_name='关注者')
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=STATUS_SHOW, verbose_name="是否显示")

    @staticmethod
    def is_followed(from_user, to_user):
        try:
            Follow.objects.get(from_user=from_user, to_user=to_user, status=Follow.STATUS_SHOW)
        except Follow.DoesNotExist:
            return False
        else:
            return True

    class Meta:
        verbose_name_plural = "关注"
        unique_together = ("from_user", "to_user")


class Notification(models.Model):
    KIND_TOPIC_ADD = 1
    KIND_REPLY_ADD = 2
    KIND_FOLLOW_ME = 3
    KIND_CHOICES = (
        (KIND_TOPIC_ADD, '发布文章'),
        (KIND_REPLY_ADD, '回复文章'),
        (KIND_FOLLOW_ME, '关注我'),
    )
    STATUS_UNREAD = 1
    STATUS_READ = 2
    STATUS_DELETE = 3
    STATUS_CHOICES = (
        (STATUS_UNREAD, '未读'),
        (STATUS_READ, '已读'),
        (STATUS_DELETE, '删除')
    )
    user = models.ForeignKey('User', related_name='notifications', verbose_name='用户')
    kind = models.IntegerField(choices=KIND_CHOICES, verbose_name="通知类型")
    status = models.IntegerField(default=STATUS_UNREAD, choices=STATUS_CHOICES, verbose_name="状态")
    content = models.TextField(default='', verbose_name='通知内容')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = "通知"


from topics.models import Favorite
