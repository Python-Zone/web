# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Topic, Section, Node, Reply, Favorite
from django.contrib import messages
from web.util import check_captcha, add_messages_from_form_errors
from users.util import login_required
from users.models import User
from .forms import TopicForm, ReplyForm


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
        "params": params,
        "from_node": ""
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
    me = request.user
    topic = get_object_or_404(Topic, pk=id_, status=Topic.STATUS_SHOW)
    user = topic.user
    if not (me.id == user.id or me.is_admin):
        raise Http404
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
    me = request.user
    topic = get_object_or_404(Topic, pk=id_, status=Topic.STATUS_SHOW)
    user = topic.user
    if not (me.id == user.id or me.is_admin):
        raise Http404
    topic.status = Topic.STATUS_DELETE
    topic.save()
    messages.success(request, '帖子已删除')
    return redirect(reverse('users.user', kwargs={"name": user.name}))


def topic_detail(request, id_):
    me = request.user
    topic = get_object_or_404(Topic, pk=id_, status=Topic.STATUS_SHOW)
    replies = Reply.objects.filter(topic=topic)
    form = ReplyForm()
    is_favorite = Favorite.is_favorite(me, topic) if me.is_authenticated() else False
    from_node = request.GET.get("from_node", "")
    publish_time = topic.publish_time
    if from_node:
        try:
            prev_topic = Topic.objects.filter(publish_time__gt=publish_time, status=Topic.STATUS_SHOW,
                                              node_id=int(from_node)).order_by('publish_time')[0]
        except IndexError:
            prev_topic = None
        try:
            next_topic = Topic.objects.filter(publish_time__lt=publish_time, status=Topic.STATUS_SHOW,
                                              node_id=int(from_node)).order_by('-publish_time')[0]
        except IndexError:
            next_topic = None
    else:
        try:
            prev_topic = Topic.objects.filter(publish_time__gt=publish_time, status=Topic.STATUS_SHOW
                                              ).order_by('publish_time')[0]
        except IndexError:
            prev_topic = None
        try:
            next_topic = Topic.objects.filter(publish_time__lt=publish_time, status=Topic.STATUS_SHOW
                                              ).order_by('-publish_time')[0]
        except IndexError:
            next_topic = None
    return render_to_response('topics/topic.html', RequestContext(request, {
        "topic": topic,
        "active_nav": "topics",
        "form": form,
        "replies": replies,
        "is_favorite": is_favorite,
        "from_node": request.GET.get("from_node",""),
        "prev_topic": prev_topic,
        "next_topic": next_topic
    }))


@login_required
def reply_add(request, topic_id):
    user = request.user
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.topic = topic
            reply.user = user
            reply.save()
            # 更新topic
            topic.last_reply_user = user
            topic.replies_count = topic.replies.count()
            topic.reply_time = reply.create_time
            topic.save()
            return render_to_response('topics/reply.html', RequestContext(request, {
                "topic": topic,
                "reply": reply,
                "floor": topic.replies.count()
            }))


@login_required
def reply_edit(request, topic_id, reply_id):
    me = request.user
    topic = get_object_or_404(Topic, pk=topic_id)
    reply = get_object_or_404(Reply, pk=reply_id, status=Reply.STATUS_SHOW)
    if not (me.id == reply.user.id or me.is_admin):
        raise Http404

    if request.method == 'GET':
        form = ReplyForm(instance=reply)
        return render_to_response('topics/reply_edit.html', RequestContext(request, {
            "topic": topic,
            "reply": reply,
            "form": form
        }))
    elif request.method == 'POST':
        form = ReplyForm(request.POST, instance=reply)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.save()
            messages.success(request, '回帖编辑成功')
            return redirect(reverse('topics.topic_detail', kwargs={"id_": topic.id}))


@login_required
def reply_delete(request, topic_id, reply_id):
    me = request.user
    topic = get_object_or_404(Topic, pk=topic_id)
    reply = get_object_or_404(Reply, pk=reply_id)
    if not (me.id == reply.user.id or me.is_admin):
        raise Http404
    reply.status = Reply.STATUS_DELETE
    reply.save()
    messages.success(request, '回帖删除成功')
    return redirect(reverse('topics.topic_detail', kwargs={"id_": topic.id}))


def node_list(request, id_):
    params = request.GET.copy()
    node = get_object_or_404(Node, pk=id_)
    _obj_list = Topic.objects.filter(node=node, status=Topic.STATUS_SHOW).order_by('-publish_time')

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

    params["from_node"] = node.id
    return render_to_response('topics/node_list.html', RequestContext(request, {
        "node": node,
        "topics": topics,
        "active_nav": "topics",
        "params": params,
        "from_node": node.id
    }))




@csrf_exempt
@login_required
def topic_favorite(request, topic_id):
    me = request.user
    topic = get_object_or_404(Topic, pk=topic_id)
    Favorite.objects.update_or_create(user=me, topic=topic, defaults={"status": Favorite.STATUS_SHOW})
    return JsonResponse({'ret': 0, 'message': '收藏成功!'})


@csrf_exempt
@login_required
def topic_unfavorite(request, topic_id):
    me = request.user
    topic = get_object_or_404(Topic, pk=topic_id)
    Favorite.objects.update_or_create(user=me, topic=topic, defaults={"status": Favorite.STATUS_DELETE})
    return JsonResponse({'ret': 0, 'message': '成功取消收藏!'})