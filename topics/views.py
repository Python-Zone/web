from django.shortcuts import render

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Topic
# Create your views here.


def topic_list(request):
    params = request.GET.copy()
    _obj_list = Topic.objects.all().order_by('-publish_time')

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
        "params": params
    }))


def topic(request):
    return render_to_response('index.html', RequestContext(request, {}))