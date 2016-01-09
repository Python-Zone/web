# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from datetime import datetime
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from web.util import check_captcha
from topics.models import Topic
from .forms import UserForm
from .models import User
from .util import login_required


def signup(request):
    if request.method == 'GET':
        captcha_key = CaptchaStore.generate_key()
        captcha_image = captcha_image_url(captcha_key)
        return render_to_response('users/user_signup.html', RequestContext(request, {
            "active_nav": "",
            "captcha_key": captcha_key,
            "captcha_image": captcha_image,

        }))
    elif request.method == 'POST':
        form = UserForm(request.POST)
        # 检查验证码
        params = request.POST.copy()
        is_captcha_ok = check_captcha(params.get('captcha_key', None), params.get('captcha', None))
        if is_captcha_ok:
            if form.is_valid():
                new_user = User.objects.create_user(name=form.cleaned_data['name'],
                                                    nickname=form.cleaned_data['nickname'],
                                                    password=form.cleaned_data['password'])
                new_user.avatar = form.cleaned_data['avatar']
                new_user.email = form.cleaned_data['email']
                new_user.save()
                return redirect('users.signin')
            else:
                return redirect('users.signup')
        else:
            return redirect('users.signup')


def signin(request):
    if request.method == 'GET':
        captcha_key = CaptchaStore.generate_key()
        captcha_image = captcha_image_url(captcha_key)
        return render_to_response('users/user_signin.html', RequestContext(request, {
            "active_nav": "",
            "captcha_key": captcha_key,
            "captcha_image": captcha_image,

        }))
    elif request.method == 'POST':
        params = request.POST.copy()
        is_captcha_ok = check_captcha(params.get('captcha_key', None), params.get('captcha', None))
        if is_captcha_ok:
            user = authenticate(name=params.get('name', None), password=params.get('password', None))
            if user and user.is_active:
                login(request, user)
                return redirect('users.user_home', name=user.name)

        return redirect('users.signin')


def signout(request):
    logout(request)
    return redirect('%s?next=/' % settings.LOGIN_URL)


@login_required
def user_home(request, name=None):
    me = request.user
    topics = Topic.objects.filter(user=me, status=Topic.STATUS_SHOW)
    return render_to_response('users/user.html', RequestContext(request, {
        "active_nav": "",
        "user": me,
        "active_tab": "topics",
        "topics": topics
    }))


@login_required
def user_replies(request, name=None):
    me = request.user
    topics = Topic.objects.filter(user=me)
    return render_to_response('users/user.html', RequestContext(request, {
        "active_nav": "",
        "user": me,
        "active_tab": "replies",
        "topics": topics
    }))