import time
import os
from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': '',
        'Показать содержимое рабочей директории': ''
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    oslist = f"Все папки и файлы: {os.listdir()}"
    return HttpResponse(oslist)
