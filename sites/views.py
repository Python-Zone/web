from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Site


def site_list(request):
    sites = []
    for kind in Site.KIND_CHOICES:
        sub_sites = Site.objects.filter(kind=kind[0]).order_by('-weight')
        sites.append((kind, sub_sites))

    return render_to_response('sites/site_list.html', RequestContext(request, {
        "sites": sites,
        "active_nav": "sites"
    }))


def site(request):
    return render_to_response('index.html', RequestContext(request, {}))