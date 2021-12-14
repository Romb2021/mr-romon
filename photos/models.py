from django.db import models
from mysite.utilities import get_timestamp_path
# from main.models import AdvUser
from projects.models import Project

class Photos(models.Model):
    title = models.CharField('Название фото',max_length=50)
    # autor = models.ForeignKey(AdvUser, on_delete=models.CASCADE, verbose_name='Автор проекта')
    autor = models.CharField('Автор',max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Изображение')    
    date = models.DateTimeField('Дата публикации')    

    def __str__(self):
        return self.title

    def get_absolute_url(self):        
        return f'/photos/{self.id}'

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'