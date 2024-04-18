from django import forms
from .models import Birthday
from django.core.exceptions import ValidationError

BEATLES = {'Джон Леннон', 'Пол Маккарти', 'Джордж Харрисон', 'Ринго Старр'}

class BirthdayForm(forms.ModelForm):
    # first_name = forms.CharField(label='Имя', max_length=20)
    # last_name = forms.CharField(
    #     label='Фамилия', help_text='Необязательное поле', required=False
    #     )
    # birthday = forms.DateField(
    #     label='Дата рождения',
    #     widget=forms.DateInput(attrs={'type':'date'})
    #     )
    class Meta:
        model = Birthday
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]
    
    def clean(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        # Проверяем вхождение сочетания имени и фамилии во множество имён.
        if f'{first_name} {last_name}' in BEATLES:
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )         