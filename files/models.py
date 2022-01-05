from django.db import models
from mysite.utilities import get_timestamp_path
# from main.models import AdvUser
from projects.models import Project

class Files(models.Model):
    file = models.FileField(blank=True, upload_to=get_timestamp_path, verbose_name='Файл')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект файла')
    describe = models.CharField('Описание файла',max_length=50, blank=True)
    date = models.DateTimeField('Дата публикации')    

    def __str__(self):
        return self.title

    def get_absolute_url(self):        
        return f'/files/{self.id}'

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'