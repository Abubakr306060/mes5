# Generated by Django 5.0.2 on 2024-02-18 15:57

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок новости')),
                ('descriptions', models.TextField(verbose_name='Описание новости')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='image/')),
                ('create', models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания новости')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='logo/', verbose_name='Логотип')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок для фотографии')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Почта')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('telegram', models.URLField(blank=True, max_length=255, null=True, verbose_name='Telegram')),
            ],
            options={
                'verbose_name': 'Настройки сайта',
                'verbose_name_plural': 'Настройки сайта ',
            },
        ),
    ]
