# Generated by Django 3.2.8 on 2021-11-07 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_photos_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='image',
        ),
    ]
