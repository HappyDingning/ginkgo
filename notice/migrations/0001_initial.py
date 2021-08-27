# Generated by Django 2.2.7 on 2019-11-06 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('date', models.DateField(auto_now_add=True, verbose_name='发表日期')),
                ('author', models.DateField(max_length=20, verbose_name='作者')),
                ('source', models.DateField(max_length=20, verbose_name='来源')),
                ('text', models.TextField(verbose_name='正文')),
            ],
        ),
    ]
