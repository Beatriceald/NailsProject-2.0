from django.http import HttpResponse
from django.shortcuts import render
from . models import *

def index(request):
    main_page = MainPage.objects.all()
    context = {
        'main_page': main_page,
        'title': 'Главная страница',
        'nbar': 'home'
    }
    return render(request, 'nails/index.html', context=context)
# Create your views here.

def show_masters(request):
    master = Master.objects.all()
    context = {
        'master': master,
        'title': 'Выбор мастера',
        'nbar': 'masters'
    }
    return render(request, 'nails/masters.html', context=context)

def show_services(request):
    return HttpResponse("Отображение услуг")

def show_reg(request):
    return HttpResponse("Отображение записи")