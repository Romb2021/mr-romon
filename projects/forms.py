from .models import Project
from django.forms import ModelForm, FileField, TextInput, DateTimeInput, Textarea
from django import forms
from django .core import validators

class ProjectForm(ModelForm):
    image = forms.ImageField(label='Изoбpaжeниe',
    validators=[validators.FileExtensionValidator(allowed_extensions=('gif', 'jpg', 'png'))], 
    error_messages={'invalid_extension':'Этот формат файлов не поддерживается'})   

    file = forms.FileField(label='Файл',
    validators=[validators.FileExtensionValidator(allowed_extensions=('docx', 'pdf', 'zip', '.jpg'))], 
    error_messages={'invalid_extension':'Этот формат файлов не поддерживается'})

    class Meta:
        model = Project        
        fields = '__all__'