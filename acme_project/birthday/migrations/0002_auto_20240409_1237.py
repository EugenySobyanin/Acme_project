# Generated by Django 3.2.16 on 2024-04-09 09:37

import birthday.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthday',
            name='image',
            field=models.ImageField(blank=True, upload_to='birthdays_images', verbose_name='Фото красавчика'),
        ),
        migrations.AlterField(
            model_name='birthday',
            name='birthday',
            field=models.DateField(validators=[birthday.validators.real_age], verbose_name='Дата рождения'),
        ),
    ]
