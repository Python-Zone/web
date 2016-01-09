# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager


class User(AbstractBaseUser):
    name = models.CharField(max_length=30, unique=True)
    #password = models.CharField(max_length=128)
    nickname = models.CharField(max_length=100)
    email = models.CharField(default='', blank=True, null=True, max_length=100)
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


    class Meta:
        verbose_name_plural = "用户"

