from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Wiki


def wiki_list(request):
    wikis = []
    for kind in Wiki.KIND_CHOICES:
        sub_wikis = Wiki.objects.filter(kind=kind[0]).order_by('-weight')
        wikis.append((kind, sub_wikis))

    return render_to_response('wiki/wiki_list.html', RequestContext(request, {
        "wikis": wikis,
        "active_nav": "wiki"
    }))


def wiki(request):
    return render_to_response('index.html', RequestContext(request, {}))