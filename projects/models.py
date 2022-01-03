from django.db import models
# from main.models import AdvUser
from mysite.utilities import get_timestamp_path

class Project(models.Model):
    title = models.CharField('Название',max_length=50)
    # autor = models.ForeignKey(AdvUser, on_delete=models.CASCADE, verbose_name='Автор проекта')
    autor = models.CharField('Автор',max_length=200)
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Изображение')    
    full_text = models.TextField('Проект')
    date = models.DateTimeField('Дата публикации')    

    def __str__(self):
        return self.title

    def get_absolute_url(self):        
        return f'/projects/{self.id}'

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)
        
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'