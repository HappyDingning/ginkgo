# Generated by Django 2.2.7 on 2020-07-02 01:46

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=10, verbose_name='类别')),
            ],
            options={
                'verbose_name': '类别',
                'verbose_name_plural': '类别',
            },
        ),
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('date', models.DateField(verbose_name='发表日期')),
                ('author', models.CharField(blank=True, max_length=20, null=True, verbose_name='作者')),
                ('source', models.CharField(blank=True, max_length=20, null=True, verbose_name='来源')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='正文')),
                ('tag', models.ManyToManyField(to='article.tag', verbose_name='分类')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]