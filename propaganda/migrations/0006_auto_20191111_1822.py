# Generated by Django 2.2.7 on 2019-11-11 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propaganda', '0005_auto_20191111_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='counselor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='指导老师'),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='members',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='参加成员'),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.news', verbose_name='关联新闻'),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='outline',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='概述'),
        ),
    ]