# Generated by Django 4.0.4 on 2022-05-06 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterservice',
            name='registration',
            field=models.ManyToManyField(blank=True, to='nails.registration'),
        ),
    ]
