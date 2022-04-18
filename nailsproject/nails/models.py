from distutils.command.upload import upload
from django.db import models
from django.urls import reverse

class MainPage(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок главной страницы')
    description_upper = models.TextField(blank=True, verbose_name='Описание главной страницы над фотографиями')
    picture1 = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", verbose_name='Фотография на странице')
    picture2 = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", verbose_name='Фотография на странице')
    picture3 = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", verbose_name='Фотография на странице')
    description_under = models.TextField(blank=True, verbose_name='Описание главной страницы под фотографиями')
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главные страницы'
        
# Create your models here.
class Master(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя мастера')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото мастера')
    grade = models.CharField(max_length=50, verbose_name='Занимаемая должность', null=True)
    experience = models.CharField(max_length=50, verbose_name='Стаж', null=True)
    rating = models.IntegerField(default=1, verbose_name='Рейтинг мастера') #нужно придумать что делать с рейтингом!
    description = models.TextField(max_length=500, verbose_name='О мастере')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('master', kwargs={'master_id': self.pk})

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'

class Service(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование услуги')
    duration = models.DurationField(verbose_name='Продолжительность')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('service', kwargs={'service_id': self.pk})

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'