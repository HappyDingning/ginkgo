# Generated by Django 2.2.7 on 2020-03-05 04:41

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20191114_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='cover_img',
            field=models.ImageField(blank=True, null=True, upload_to='news_cover', verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=tinymce.models.HTMLField(verbose_name='正文'),
        ),
    ]