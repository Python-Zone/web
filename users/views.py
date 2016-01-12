# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from datetime import datetime
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.contrib import messages
from web.util import check_captcha, add_messages_from_form_errors
from topics.models import Topic, Reply
from .forms import UserForm
from .models import User, Follow, Favorite
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


def common_info(request, me, user):
    if me.is_authenticated() and me.id != user.id:
        return {
            "is_followed": Follow.is_followed(me, user)
        }
    else:
        return {}


def user_home(request, name=None):
    context = {}
    params = request.GET.copy()
    user = get_object_or_404(User, name=name)
    _obj_list = Topic.objects.filter(user=user).order_by('-publish_time')

    paginator = Paginator(_obj_list, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        topics = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        topics = paginator.page(paginator.num_pages)

    context.update(common_info(request, request.user, user))
    context.update( {
        "active_nav": "",
        "visited_user": user,
        "active_tab": "topics",
        "topics": topics,
        "params": params
    })
    return render_to_response('users/user.html', RequestContext(request, context))


def user_replies(request, name=None):
    context = {}
    params = request.GET.copy()
    user = get_object_or_404(User, name=name)
    _obj_list = Reply.objects.filter(user=user).order_by('-id')

    paginator = Paginator(_obj_list, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        replies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        replies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        replies = paginator.page(paginator.num_pages)

    context.update(common_info(request, request.user, user))
    context.update({
        "active_nav": "",
        "visited_user": user,
        "active_tab": "replies",
        "replies": replies,
        "params": params
    })

    return render_to_response('users/user_replies.html', RequestContext(request, context))


def user_following(request, name):
    context = {}
    params = request.GET.copy()
    user = get_object_or_404(User, name=name)
    _obj_list = Follow.objects.filter(from_user=user).order_by('-id')

    paginator = Paginator(_obj_list, 30)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        followings = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        followings = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        followings = paginator.page(paginator.num_pages)

    context.update(common_info(request, request.user, user))
    context.update( {
        "active_nav": "",
        "visited_user": user,
        "active_tab": "following",
        "followings": followings,
        "params": params
    })
    return render_to_response('users/user_following.html', RequestContext(request, context))


def user_followers(request, name):
    context = {}
    params = request.GET.copy()
    user = get_object_or_404(User, name=name)
    _obj_list = Follow.objects.filter(to_user=user).order_by('-id')

    paginator = Paginator(_obj_list, 30)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        followers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        followers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        followers = paginator.page(paginator.num_pages)

    # 添加关注信息
    for item in followers.object_list:
        item.is_followed = Follow.is_followed(user, item.from_user)
    context.update(common_info(request, request.user, user))
    context.update( {
        "active_nav": "",
        "visited_user": user,
        "active_tab": "followers",
        "followers": followers,
        "params": params
    })
    return render_to_response('users/user_followers.html', RequestContext(request, context))


@csrf_exempt
@login_required
def user_follow(request, name):
    me = request.user
    user = get_object_or_404(User, name=name)
    try:
        Follow.objects.create(from_user=me, to_user=user)
    except Exception as e:
        return JsonResponse({'ret': 1, 'message': '不能重复关注!'})
    else:
        return JsonResponse({'ret': 0, 'message': '关注成功!'})


@csrf_exempt
@login_required
def user_unfollow(request, name):
    me = request.user
    user = get_object_or_404(User, name=name)
    try:
        Follow.objects.filter(from_user=me, to_user=user).delete()
    except Exception as e:
        return JsonResponse({'ret': 1, 'message': '取消关注失败'})
    else:
        return JsonResponse({'ret': 0, 'message': '成功取消关注!'})