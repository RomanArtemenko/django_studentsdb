# -*- coding UTF-8 -*-

from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext, loader
# Create your views here.

def students_list(request):
    students = (
        {'id' : 1,
         'first_name' : u'Сергій',
         'last_name' : u'Солод',
         'ticket' : 2351,
         'image' : 'img/solod.jpg'},
        {'id' : 2,
         'first_name' : u'Роман',
         'last_name' : u'Артеменко',
         'ticket' : 8729,
         'image' : 'img/me.jpg'},
        {'id' : 3,
         'first_name' : u'Александр',
         'last_name' : u'Калмиков',
         'ticket' : 3621,
         'image' : 'img/kalmikov.jpg'}
    )
    return render(request,'students/students_list.html', {'students' : students})

def student_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' %sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' %sid)

def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')

def groups_add(request):
    return HttpResponse('<h1>Groups Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' %gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' %gid)