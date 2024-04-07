from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def projects(request):
    return HttpResponse('Return all http responses')

def project(request, project_id):
    return HttpResponse(f'Return project {project_id}')
