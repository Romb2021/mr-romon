# Generated by Django 3.2.10 on 2022-01-25 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name': 'Блог', 'verbose_name_plural': 'Блоги'},
        ),
        migrations.AddField(
            model_name='blogpost',
            name='url_link',
            field=models.URLField(blank=True),
        ),
    ]
