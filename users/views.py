# -*- coding: utf-8 -*-
__author__ = 'yijingping'
import json
from datetime import datetime
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.urlresolvers import reverse
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
from topics.models import Topic, Reply, Favorite
from .forms import UserForm
from .models import User, Follow, Notification
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
    _obj_list = Follow.objects.filter(from_user=user, status=Follow.STATUS_SHOW).order_by('-id')

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
    _obj_list = Follow.objects.filter(to_user=user, status=Follow.STATUS_SHOW).order_by('-id')

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
    Follow.objects.update_or_create(from_user=me, to_user=user, defaults={"status": Follow.STATUS_SHOW})
    return JsonResponse({'ret': 0, 'message': '关注成功!'})


@csrf_exempt
@login_required
def user_unfollow(request, name):
    me = request.user
    user = get_object_or_404(User, name=name)
    Follow.objects.update_or_create(from_user=me, to_user=user, defaults={"status": Follow.STATUS_DELETE})
    return JsonResponse({'ret': 0, 'message': '成功取消关注!'})


def user_favorites(request, name):
    context = {}
    params = request.GET.copy()
    user = get_object_or_404(User, name=name)
    _obj_list = Favorite.objects.filter(user=user).order_by('-id')

    paginator = Paginator(_obj_list, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        favorites = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        favorites = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        favorites = paginator.page(paginator.num_pages)

    context.update(common_info(request, request.user, user))
    context.update( {
        "active_nav": "",
        "visited_user": user,
        "active_tab": "favorites",
        "favorites": favorites,
        "params": params
    })
    return render_to_response('users/user_favorites.html', RequestContext(request, context))


@login_required
def notifications(request):
    user = request.user
    context = {}
    params = request.GET.copy()
    _obj_list = Notification.objects.filter(user=user).exclude(status=Notification.STATUS_DELETE).order_by('-id')

    paginator = Paginator(_obj_list, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        notifications = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        notifications = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        notifications = paginator.page(paginator.num_pages)

    # 添加通知详情信息
    for item in notifications.object_list:
        #item.status = Notification.STATUS_READ
        #item.save()
        content = json.loads(item.content)
        if item.kind == Notification.KIND_TOPIC_ADD:
            item.topic = get_object_or_404(Topic, pk=content["topic_id"])
        elif item.kind == Notification.KIND_REPLY_ADD:
            item.reply = get_object_or_404(Reply, pk=content["reply_id"])
        elif item.kind == Notification.KIND_FOLLOW_ME:
            item.follow = get_object_or_404(Topic, pk=content["follow_id"])

    context.update(common_info(request, request.user, user))
    context.update({
        "active_nav": "",
        "notifications": notifications,
        "params": params
    })

    return render_to_response('users/notifications.html', RequestContext(request, context))


@login_required
def notifications_unread(request):
    user = request.user
    context = {}
    params = request.GET.copy()
    _obj_list = Notification.objects.filter(user=user, status=Notification.STATUS_UNREAD).order_by('-id')

    paginator = Paginator(_obj_list, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        notifications = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        notifications = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        notifications = paginator.page(paginator.num_pages)

    # 添加通知详情信息
    for item in notifications.object_list:
        #item.status = Notification.STATUS_READ
        #item.save()
        content = json.loads(item.content)
        if item.kind == Notification.KIND_TOPIC_ADD:
            item.topic = get_object_or_404(Topic, pk=content["topic_id"])
        elif item.kind == Notification.KIND_REPLY_ADD:
            item.reply = get_object_or_404(Reply, pk=content["reply_id"])
        elif item.kind == Notification.KIND_FOLLOW_ME:
            item.follow = get_object_or_404(Topic, pk=content["follow_id"])

    context.update(common_info(request, request.user, user))
    context.update({
        "active_nav": "",
        "notifications": notifications,
        "params": params
    })

    return render_to_response('users/notifications.html', RequestContext(request, context))


@login_required
def notifications_clear(request):
    user = request.user
    Notification.objects.filter(user=user).update(status=Notification.STATUS_DELETE)
    messages.success(request, '成功清除所有消息通知!')
    return redirect(reverse('users.notifications'))


@csrf_exempt
@login_required
def notifications_delete(request, id_):
    me = request.user
    matched_rows = Notification.objects.filter(pk=id_, user=me).update(status=Notification.STATUS_DELETE)
    if matched_rows > 0:
        return JsonResponse({'ret': 0, 'message': '成功删除消息!'})
    else:
        return JsonResponse({'ret': 1, 'message': '消息不存在!'})

