from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
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

def show_masters(request): # Отображение страницы с выбором мастеров
    master = Master.objects.all()
    context = {
        'master': master,
        'title': 'Выбор мастера',
        'nbar': 'masters'
    }
    return render(request, 'nails/masters.html', context=context)


def show_master(request, master_id):  # Отображение страницы мастера
    
    master = get_object_or_404(Master, pk=master_id)
    service = Service.objects.all()

    context = {
        'master': master,
        'service': service,
        'title': 'Подробнее о мастере',
        'nbar': 'masters'
    }
    return render(request, 'nails/master.html', context=context)


def show_services(request):
    return HttpResponse("Отображение услуг")

def show_reg(request):
    return HttpResponse("Отображение записи")


