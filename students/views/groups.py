# -*- coding UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def groups_list(request):
    groups = (
        {'id' : 1,
         'name' : u'СП - 1',
         'starosta' : u'Артеменко Роман'},
        {'id' : 2,
         'name' : u'СП - 2',
         'starosta' : u'Калмиков Александр'},
        {'id' : 3,
         'name' : u'ЕС - 1',
         'starosta' : u'Солод Сергій'}
    )
    return render(request, 'students/groups_list.html', {'groups' : groups})

def groups_add(request):
    return HttpResponse('<h1>Groups Add Form</h1>')
    #return HttpResponse('<h1>'{request.path}'</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' %gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' %gid)
