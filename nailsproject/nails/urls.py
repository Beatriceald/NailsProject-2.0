from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('masters/', show_masters, name='masters'),
    path('services/', show_services, name='services'),
    path('registration/', RegistrationCreateView.as_view(), name='reg'),
    path('master/<int:master_id>/', show_master, name='master'),
    path('registration/<int:registration_id>', ShowRegistration.as_view(), name='confirmation')
]