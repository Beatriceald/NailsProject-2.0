# Generated by Django 4.0.4 on 2022-04-20 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nails', '0007_remove_service_duration_remove_service_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterservice',
            name='duration',
            field=models.IntegerField(verbose_name='Продолжительность в минутах'),
        ),
    ]
