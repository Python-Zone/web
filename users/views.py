# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from datetime import datetime
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.contrib import messages
from web.util import check_captcha, add_messages_from_form_errors
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
            "captcha_image": captcha_image
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
                messages.success(request, "登录成功")
                # 自动登录
                user = authenticate(name=form.cleaned_data['name'], password=form.cleaned_data['password'])
                if user and user.is_active:
                    login(request, user)
                    messages.success(request, "注册成功")
                    return redirect('users.user', name=user.name)
            else:
                add_messages_from_form_errors(request, form)
        else:
            messages.error(request, "验证码错误")
        # 带着form信息,重新注册
        captcha_key = CaptchaStore.generate_key()
        captcha_image = captcha_image_url(captcha_key)
        return render_to_response('users/user_signup.html', RequestContext(request, {
            "active_nav": "",
            "captcha_key": captcha_key,
            "captcha_image": captcha_image,
            "form": form
        }))


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
                messages.success(request, "登录成功")
                return redirect('users.user', name=user.name)
            else:
                messages.error(request, "用户名或密码错误,亲重试")
        else:
            messages.error(request, "验证码错误")

        return redirect('users.signin')


def signout(request):
    logout(request)
    messages.success(request, "退出成功")
    return redirect('index')


def captcha_refresh(request):
    captcha_key = CaptchaStore.generate_key()
    captcha_image = captcha_image_url(captcha_key)
    return JsonResponse({
        "captcha_key": captcha_key,
        "captcha_image": captcha_image,

    })


def user_home(request, name=None):
    user = get_object_or_404(User, name=name)
    topics = Topic.objects.filter(user=user, status=Topic.STATUS_SHOW)
    return render_to_response('users/user.html', RequestContext(request, {
        "active_nav": "",
        "user": user,
        "active_tab": "topics",
        "topics": topics
    }))


@login_required
def user_replies(request, name=None):
    user = get_object_or_404(User, name=name)
    topics = Topic.objects.filter(user=user)
    return render_to_response('users/user.html', RequestContext(request, {
        "active_nav": "",
        "user": user,
        "active_tab": "replies",
        "topics": topics
    }))