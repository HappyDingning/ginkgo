# Generated by Django 2.2.7 on 2019-11-18 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_user_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='photo',
            field=models.ImageField(blank=True, default='photo/default_avatar.png', upload_to='photo', verbose_name='头像'),
        ),
    ]
