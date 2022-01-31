from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    url_link = models.URLField(blank=True ,max_length=200)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'