# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-01 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_auto_20160801_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_desc',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_tags',
            field=models.TextField(default=None),
        ),
    ]