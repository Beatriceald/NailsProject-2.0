from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('masters/', show_masters, name='masters'),
    path('services/', show_services, name='services'),
    path('registration/', show_reg, name='reg'),
    path('master/<int:master_id>/', show_master, name='master'),
]