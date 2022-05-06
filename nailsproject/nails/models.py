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
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото мастера')
    grade = models.CharField(max_length=50, verbose_name='Занимаемая должность', null=True)
    experience = models.CharField(max_length=50, verbose_name='Стаж', null=True)
    rating = models.IntegerField(default=1, verbose_name='Рейтинг мастера') #нужно придумать что делать с рейтингом!
    description = models.TextField(max_length=500, verbose_name='О мастере')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('master', kwargs={'master_slug': self.slug})

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'

class Service(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Наименование услуги')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service', kwargs={'service_id': self.pk})

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class MasterService(models.Model):
    master = models.ForeignKey(Master, on_delete=models.PROTECT, verbose_name='Мастер')
    services = models.ForeignKey(Service, on_delete=models.PROTECT, verbose_name='Услуга')
    duration = models.IntegerField(verbose_name='Продолжительность в минутах')
    price = models.IntegerField(verbose_name='Цена')
    registration = models.ManyToManyField('Registration', blank=True)
        #ManyToManyField или ForeignKey!!!
    def __str__(self):
        return f'{self.services}' 

    class Meta:
        verbose_name = 'Продолжительность и цена услуги'
        verbose_name_plural = 'Продолжительность и цена услуги'

class Registration(models.Model):
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    users_name = models.CharField(max_length=100, verbose_name='ФИО')
    reg_date = models.DateField(null=True, verbose_name='Дата записи')
    reg_time = models.TimeField(null=True, verbose_name='Время записи')

    def get_absolute_url(self):
        return reverse('confirmation', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.users_name}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Запись'
