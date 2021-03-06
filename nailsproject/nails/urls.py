from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('masters/', show_masters, name='masters'),
    path('services/', show_services, name='services'),
    path('registration/', RegistrationCreateView.as_view(), name='reg'),
    path('master/<slug:master_slug>/', show_master, name='master'),
    path('registration/<int:pk>', ShowRegistration.as_view(), name='confirmation')
]