# Generated by Django 3.2.8 on 2021-11-04 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20211025_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='autor',
            field=models.CharField(max_length=200, verbose_name='Автор'),
        ),
    ]
