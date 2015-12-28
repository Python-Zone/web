# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Config(models.Model):
    """
    微信参数
    """
    TYPE_TOKEN = 0
    TYPE_TICKET = 1
    type = models.IntegerField(verbose_name="参数类型")
    value = models.TextField(null=True, verbose_name='参数值')
