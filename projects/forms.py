from .models import Project
from photos.models import Photos
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, URLField
from django import forms
from django .core import validators
# from main.models import Img

class ProjectForm(ModelForm):
    image = forms.ModelChoiceField(queryset=Photos.objects.all(),
    label='Фото', help_text='He забудьте задать фото!')    

    class Meta:
        model = Project        
        fields = '__all__'

        widgets = {
            'title': TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Название проекта'
            }),
            'autor': TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Автор проекта'
            }),
            'full_text': Textarea(attrs={
                'class':'form-control',
                'placeholder': 'Текст проекта'
            }),
            'date': DateTimeInput(attrs={
                'class':'form-control',
                'placeholder': 'Дата публикации'       
            })
        }