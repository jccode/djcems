# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 08:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0005_auto_20151223_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='drivers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='\u53f8\u673a'),
        ),
    ]
