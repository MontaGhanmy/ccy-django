# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-01 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_userprofile_user_successrate'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_description',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_tags',
            field=models.TextField(default=None),
        ),
    ]
