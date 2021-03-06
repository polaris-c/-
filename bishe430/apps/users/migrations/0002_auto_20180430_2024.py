# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-30 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picUrl',
            field=models.ImageField(blank=True, null=True, upload_to='image/user/', verbose_name='头像路径'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.IntegerField(choices=[(1, '超级管理员'), (2, '管理员'), (3, '普通用户')], default=3, help_text='权限标识', verbose_name='权限标识'),
        ),
    ]
