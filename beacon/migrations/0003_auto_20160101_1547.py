# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0002_auto_20160101_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beacon',
            name='stick_on',
            field=models.ManyToManyField(blank=True, null=True, to='vehicle.Bus', verbose_name='Stick on'),
        ),
    ]
