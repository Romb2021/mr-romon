
from files.models import Files
from projects.models import Project
from django import forms
from django .core import validators

class FileForm(forms.ModelForm):
    file = forms.FileField(label='Файл',
    validators=[validators.FileExtensionValidator(allowed_extensions=('docx', 'pdf', 'zip', 'jpg'))], 
    error_messages={'invalid_extension':'Этот формат файлов не поддерживается'})

    project = forms.ModelChoiceField(queryset=Project.objects.all(),
    label='Проект', help_text='He забудьте задать проект!',
    widget=forms.widgets.Select(attrs={'size': 3}))
    
    class Meta:
        model = Files        
        fields = "__all__"