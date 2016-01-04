from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from .models import Job
# Create your views here.

def job_list(request):
    params = request.GET.copy()
    city = params.get('city', None)
    if city:
        _obj_list = Job.objects.filter(city=city).order_by('-publish_time')
    else:
        _obj_list = Job.objects.all().order_by('-publish_time')

    paginator = Paginator(_obj_list, 20)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        jobs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        jobs = paginator.page(paginator.num_pages)

    citys = list(Job.objects.values('city').annotate(num=Count('city')).order_by('-num'))[:10]
    return render_to_response('jobs/job_list.html', RequestContext(request, {
        "jobs": jobs,
        "citys": citys,
        "active_nav": "jobs",
        "params": params
    }))

def job(request):
    return render_to_response('index.html', RequestContext(request, {}))