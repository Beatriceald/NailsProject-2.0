# Generated by Django 4.0.4 on 2022-05-06 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок главной страницы')),
                ('description_upper', models.TextField(blank=True, verbose_name='Описание главной страницы над фотографиями')),
                ('picture1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фотография на странице')),
                ('picture2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фотография на странице')),
                ('picture3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фотография на странице')),
                ('description_under', models.TextField(blank=True, verbose_name='Описание главной страницы под фотографиями')),
            ],
            options={
                'verbose_name': 'Главная страница',
                'verbose_name_plural': 'Главные страницы',
            },
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя мастера')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото мастера')),
                ('grade', models.CharField(max_length=50, null=True, verbose_name='Занимаемая должность')),
                ('experience', models.CharField(max_length=50, null=True, verbose_name='Стаж')),
                ('rating', models.IntegerField(default=1, verbose_name='Рейтинг мастера')),
                ('description', models.TextField(max_length=500, verbose_name='О мастере')),
            ],
            options={
                'verbose_name': 'Мастер',
                'verbose_name_plural': 'Мастера',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('users_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('reg_date', models.DateField(null=True, verbose_name='Дата записи')),
                ('reg_time', models.TimeField(null=True, verbose_name='Время записи')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Запись',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, verbose_name='Наименование услуги')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='MasterService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField(verbose_name='Продолжительность в минутах')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nails.master', verbose_name='Мастер')),
                ('registration', models.ManyToManyField(to='nails.registration')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nails.service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Продолжительность и цена услуги',
                'verbose_name_plural': 'Продолжительность и цена услуги',
            },
        ),
    ]
