from csv import list_dialects
from django.contrib import admin
from . models import *

class mainpageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description_upper', 'picture1', 'picture2', 'picture3', 'description_under')
    list_display_links = ('id', 'title')

class masterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'grade', 'experience', 'rating', 'description')
    list_display_links = ('name',)

class serviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)

class masterservicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'master', 'services', 'duration', 'price')
    list_display_links = ('master',)

class registrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'users_name', 'phone_number', 'reg_date', 'reg_time', 'master')
    list_display_links = ('users_name', 'reg_date', 'reg_time')

admin.site.register(MasterService, masterservicesAdmin)
admin.site.register(Service, serviceAdmin)
admin.site.register(MainPage, mainpageAdmin)
admin.site.register(Master, masterAdmin)
admin.site.register(Registration, registrationAdmin)

# Register your models here.
