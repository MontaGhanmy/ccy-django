# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-14 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createcourse', '0011_auto_20160813_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='videos',
            field=models.ManyToManyField(to='createcourse.Videos'),
        ),
    ]
