from django.db import models
from mysite.utilities import get_timestamp_path
# from main.models import AdvUser
from projects.models import Project

class Photos(models.Model):
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Изображение')    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект фото')
    describe = models.CharField('Описание фото',max_length=50, blank=True)
    date = models.DateTimeField('Дата публикации')    

    def __str__(self):
        return self.title

    def get_absolute_url(self):        
        return f'/photos/{self.id}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'