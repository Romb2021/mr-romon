# Generated by Django 3.2.8 on 2021-11-07 06:11

from django.db import migrations, models
import mysite.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_remove_photos_full_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='image',
            field=models.ImageField(blank=True, upload_to=mysite.utilities.get_timestamp_path, verbose_name='Изображение'),
        ),
    ]