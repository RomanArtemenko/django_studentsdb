# -*- coding UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def journal(request):
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
    wD = ['Пн','Вт','Ср','Чт','Пт','Сб','Вс']

    days = range(1,31)
    return render(request, 'students/journal.html', {'students' : students, 'days' : days })