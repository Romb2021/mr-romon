from .models import Articles
from projects.models import Project
from django import forms # ModelForm, TextInput, DateTimeInput, Textarea, ImageField

class ArticlesForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(),
    label='Проект', help_text='He забудьте задать проект!',
    widget=forms.widgets.Select(attrs={'size': 3}))

    class Meta:
        model = Articles        
        fields = ['title','project','full_text','date']        

        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Название статьи'
            }),
            'full_text': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder': 'Текст статьи'
            }),
            'date': forms.DateTimeInput(attrs={
                'class':'form-control',
                'placeholder': 'Дата публикации'       
            })
        }