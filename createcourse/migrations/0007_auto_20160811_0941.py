# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-11 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createcourse', '0006_auto_20160811_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='avability_end_time_period',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='avability_start_time_period',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
