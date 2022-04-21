from csv import list_dialects
from django.contrib import admin
from . models import *

class mainpageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description_upper', 'picture1', 'picture2', 'picture3', 'description_under')
    list_display_links = ('id', 'title')

class masterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'grade', 'experience', 'rating', 'description')
    list_display_links = ('id', 'name')

class serviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class masterservicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'master', 'services', 'duration', 'price')


admin.site.register(MasterService, masterservicesAdmin)
admin.site.register(Service, serviceAdmin)
admin.site.register(MainPage, mainpageAdmin)
admin.site.register(Master, masterAdmin)

# Register your models here.
