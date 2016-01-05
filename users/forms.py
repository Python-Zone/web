# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django import forms
from django.forms import ModelForm
from .models import User
from captcha.fields import CaptchaField


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ['is_active', 'is_admin', 'last_login', 'create_time']