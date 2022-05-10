from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from nails.forms import AddRegistrationForm
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


def show_master(request, master_slug):  # Отображение страницы мастера
    
    master = get_object_or_404(Master, slug=master_slug)
    service = Service.objects.all()
    master_service = MasterService.objects.filter(master__slug=master_slug).order_by('services__id', 'services')
    
    context = {
        'master_service': master_service,
        'master': master,
        'service': service,
        'title': 'Подробнее о мастере',
        'duration': ' минут',
        'price': ' руб',
        'part': ' / ноготь',
        'nbar': 'masters',
    }
    return render(request, 'nails/master.html', context=context)


def show_services(request):

    context = {
        'nbar': 'services'
    }

    return render(request, 'nails/services.html', context=context)

# def show_reg(request):
#     form = AddRegistrationForm()
#     return render(request, 'nails/registration.html', {'form': form, 'title': 'Запись', 'nbar': 'reg',})

class RegistrationCreateView(CreateView): # создание формы-регистрации
    form_class = AddRegistrationForm
    template_name = 'nails/registration.html'
    #success_url = reverse_lazy('confirmation')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запись'
        context['nbar'] = 'reg'
        return context


class ShowRegistration(DetailView): # вывод информации после регистрации
    model = Registration
    template_name = 'nails/confirmation.html'
    context_object_name = 'confirmation' 


    #servs = Service.objects.filter(reg__id=Registration.pk) 

    # https://djbook.ru/rel1.9/topics/db/queries.html#lookups-that-span-relationships

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Подтверждение записи"
        context['nbar'] = "reg"
        context['master'] = "Запись к мастеру: "
        context['service'] = "Запись на услуги: "
        context['duration'] = "Продолжительность сеанса: "
        context['price'] = "Стоимость услуг: "
        context['reg_serv'] = Service.objects.filter(registration__id=self.object.id)
        context['masterservice'] = MasterService.objects.filter(registration__id=self.object.id)
        return context

# def confirmation(request):
#     return render(request, 'nails/confirmation.html', context= {'title': 'Подтверждение записи', 'nbar': 'reg'})


    
# def show_reg(request):
#     master = Master.objects.all()
#     service = Service.objects.all()
#     context = {
#         'master': master,
#         'service': service,
#         'nbar': 'reg',
#     }
#     return render(request, 'nails/registration.html', context=context)
