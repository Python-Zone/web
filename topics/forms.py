# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django import forms
from .models import Topic


class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ['node', 'title', 'content']