# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createcourse', '0010_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='avability_end_date',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='avability_start_date',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
