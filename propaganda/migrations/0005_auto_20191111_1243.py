# Generated by Django 2.2.7 on 2019-11-11 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propaganda', '0004_auto_20191111_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='counselor',
            field=models.CharField(max_length=100, null=True, verbose_name='指导老师'),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='members',
            field=models.CharField(max_length=100, null=True, verbose_name='参加成员'),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='outline',
            field=models.CharField(max_length=200, null=True, verbose_name='概述'),
        ),
    ]
