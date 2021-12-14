from django.db import models
from projects.models import Project

class Articles(models.Model):
    title = models.CharField('Название',max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')        

    def __str__(self):
        return self.title

    def get_absolute_url(self):        
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'