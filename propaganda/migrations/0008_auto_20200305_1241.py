# Generated by Django 2.2.7 on 2020-03-05 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propaganda', '0007_auto_20191114_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='level',
            field=models.IntegerField(default=0, verbose_name='level'),
        ),
    ]