from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext, loader
# Create your views here.

def students_list(request):
    #return HttpResponse('<h1>Hello World</h1>')
    return render(request,'students/students_list.html', {})