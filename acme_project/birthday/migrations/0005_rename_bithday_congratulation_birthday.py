# Generated by Django 3.2.16 on 2024-05-05 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0004_congratulation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='congratulation',
            old_name='bithday',
            new_name='birthday',
        ),
    ]
