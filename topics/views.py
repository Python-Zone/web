# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Topic, Section, Node
from django.contrib import messages
from web.util import check_captcha, add_messages_from_form_errors
from users.util import login_required
from .forms import TopicForm


def topic_list(request):
    params = request.GET.copy()
    _obj_list = Topic.objects.filter(status=Topic.STATUS_SHOW).order_by('-publish_time')

    paginator = Paginator(_obj_list, 20)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        topics = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        topics = paginator.page(paginator.num_pages)

    return render_to_response('topics/topic_list.html', RequestContext(request, {
        "topics": topics,
        "active_nav": "topics",
        "sections": Section.objects.order_by('-weight'),
        "params": params
    }))


@login_required
def topic_add(request):
    if request.method == 'GET':
        form = TopicForm(initial={"node": "", "title": "", "content": ""})
        return render_to_response('topics/topic_add.html', RequestContext(request, {
            "sections": Section.objects.order_by('-weight'),
            "form": form
        }))
    elif request.method == 'POST':
        user = request.user
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = user
            topic.save()
            messages.success(request, '帖子发布成功')
            return redirect(reverse('topics.topic_detail', kwargs={"id_": topic.id}))
        else:
            add_messages_from_form_errors(request, form)
            return render_to_response('topics/topic_add.html', RequestContext(request, {
                "sections": Section.objects.order_by('-weight'),
                "form": form
            }))


@login_required
def topic_edit(request, id_):
    user = request.user
    topic = get_object_or_404(Topic, pk=id_, user=user, status=Topic.STATUS_SHOW)
    if request.method == 'GET':
        form = TopicForm(instance=topic)
        return render_to_response('topics/topic_add.html', RequestContext(request, {
            "sections": Section.objects.order_by('-weight'),
            "form": form
        }))
    elif request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = user
            topic.save()
            messages.success(request, '帖子编辑成功')
            return redirect(reverse('topics.topic_detail', kwargs={"id_": topic.id}))
        else:
            add_messages_from_form_errors(request, form)
            return render_to_response('topics/topic_add.html', RequestContext(request, {
                "sections": Section.objects.order_by('-weight'),
                "form": form
            }))


@login_required
def topic_delete(request, id_):
    user = request.user
    topic = get_object_or_404(Topic, pk=id_, user=user, status=Topic.STATUS_SHOW)
    topic.status = Topic.STATUS_DELETE
    topic.save()
    messages.success(request, '帖子已删除')
    return redirect(reverse('users.user_home', kwargs={"name": user.name}))


def topic_detail(request, id_):
    topic = get_object_or_404(Topic, pk=id_, status=Topic.STATUS_SHOW)
    return render_to_response('topics/topic.html', RequestContext(request, {
        "topic": topic,
        "active_nav": "topics"
    }))


def node_list(request, id_):
    params = request.GET.copy()
    node = get_object_or_404(Node, pk=id_)
    _obj_list = Topic.objects.filter(node=node).order_by('-publish_time')

    paginator = Paginator(_obj_list, 20)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        topics = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        topics = paginator.page(paginator.num_pages)

    return render_to_response('topics/node_list.html', RequestContext(request, {
        "node": node,
        "topics": topics,
        "active_nav": "topics",
        "params": params
    }))