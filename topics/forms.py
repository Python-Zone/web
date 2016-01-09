# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Topic


class TopicForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Topic
        fields = ['node', 'title', 'content']