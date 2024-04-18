from django.db import models
from .validators import real_age

class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия',
        help_text='Необязательное поле',
        blank=True,
        max_length=20
    )
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    image = models.ImageField('Фото красавчика', upload_to='birthdays_images', blank=True)