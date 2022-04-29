from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
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


def show_master(request, master_id):  # Отображение страницы мастера
    
    master = get_object_or_404(Master, pk=master_id)
    service = Service.objects.all()
    master_service = MasterService.objects.filter(master__id=master_id).order_by('services__id', 'services')
    
    context = {
        'master_service': master_service,
        'master': master,
        'service': service,
        'title': 'Подробнее о мастере',
        'duration': ' минут',
        'price': ' руб',
        'nbar': 'masters'
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

class RegistrationCreateView(CreateView):
    form_class = AddRegistrationForm
    template_name = 'nails/registration.html'
    success_url = reverse_lazy('confirmation')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запись'
        context['nbar'] = 'reg'
        return context

def confirmation(request):
    return render(request, 'nails/confirmation.html', context= {'nbar': 'reg'})


    
# def show_reg(request):
#     master = Master.objects.all()
#     service = Service.objects.all()
#     context = {
#         'master': master,
#         'service': service,
#         'nbar': 'reg',
#     }
#     return render(request, 'nails/registration.html', context=context)
