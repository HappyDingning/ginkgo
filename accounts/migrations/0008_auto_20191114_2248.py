# Generated by Django 2.2.7 on 2019-11-14 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20191113_1626'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': '报名申请', 'verbose_name_plural': '报名信息'},
        ),
        migrations.AlterModelOptions(
            name='user_profile',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
    ]
