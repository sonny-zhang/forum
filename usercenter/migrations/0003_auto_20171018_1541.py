# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-18 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercenter', '0002_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.CharField(blank=True, max_length=300, verbose_name='头像地址'),
        ),
    ]