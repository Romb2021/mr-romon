
from photos.models import Photos
from projects.models import Project
from django import forms
from django .core import validators

class PhotoForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(),
    label='Проект', help_text='He забудьте задать проект!',
    widget=forms.widgets.Select(attrs={'size': 3}))

    image = forms.ImageField(label='Изoбpaжeниe',
    validators=[validators . FileExtensionValidator(allowed_extensions=('gif', 'jpg', 'png'))], 
    error_messages={'invalid_extension':'Этот формат файлов не поддерживается'})    
    
    class Meta:
        model = Photos        
        fields = "__all__"