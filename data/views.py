# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http.response import JsonResponse
from .models import Community
def community_list(request):
    params = request.GET.copy()

    return render_to_response('data/community_list.html', RequestContext(request, {
        "title": "北京房价",
        "active_nav": "data",
        "params": params
    }))

def community_heat_data(request):
    coms = Community.objects.order_by('-avr_price')
    data = []
    for item in coms:
        data.append({"lng": item.lng, "lat": item.lat, "count": 5})
    return JsonResponse({
        'ret': 0,
        'data': data
    })
