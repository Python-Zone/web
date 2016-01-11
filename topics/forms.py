# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Topic, Reply


class TopicForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Topic
        fields = ['node', 'title', 'content']


class ReplyForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(config_name="reply"))

    class Meta:
        model = Reply
        fields = ['content']
