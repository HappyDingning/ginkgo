# Generated by Django 2.2.7 on 2019-11-06 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='tag_id',
            new_name='tag',
        ),
    ]
