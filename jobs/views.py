from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def job_list(request):
    return HttpResponse('job_list')


def job(request):
    return HttpResponse('job')