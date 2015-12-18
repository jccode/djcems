# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-18 15:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_bus_drivers'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnergySavingData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('energy_saving_amount', models.IntegerField(blank=True, null=True, verbose_name='Energy saving amount')),
                ('energy_saving_money', models.IntegerField(blank=True, null=True, verbose_name='Energy saving money')),
                ('emission_reduction', models.IntegerField(blank=True, null=True, verbose_name='\u51cf\u6392\u6811\u91cf')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FuelCellData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('status', models.IntegerField(blank=True, choices=[(0, '\u5de5\u4f5c\u4e2d'), (1, '\u6545\u969c'), (2, '\u505c\u6b62')], null=True, verbose_name='\u71c3\u6599\u7535\u6c60\u72b6\u6001')),
                ('voltage', models.IntegerField(blank=True, null=True, verbose_name='\u71c3\u6599\u7535\u6c60\u7535\u538b')),
                ('current', models.IntegerField(blank=True, null=True, verbose_name='\u71c3\u6599\u7535\u6c60\u7535\u6d41')),
                ('temp', models.IntegerField(blank=True, null=True, verbose_name='\u71c3\u6599\u7535\u6c60\u6e29\u5ea6')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GasData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('remain', models.IntegerField(blank=True, null=True, verbose_name='\u6c22\u6c14\u4f59\u91cf')),
                ('bottle_temp', models.IntegerField(blank=True, null=True, verbose_name='\u6c22\u6c14\u74f6\u6e29\u5ea6')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MotorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('speed', models.IntegerField(blank=True, null=True, verbose_name='Motor speed')),
                ('torque', models.IntegerField(blank=True, null=True, verbose_name='Motor torque')),
                ('voltage', models.IntegerField(blank=True, null=True, verbose_name='Motor voltage')),
                ('current', models.IntegerField(blank=True, null=True, verbose_name='Motor current')),
                ('temp', models.IntegerField(blank=True, null=True, verbose_name='Motor temperature')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PowerBatteryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('status', models.IntegerField(blank=True, null=True, verbose_name='\u52a8\u529b\u7535\u6c60\u72b6\u6001')),
                ('voltage', models.IntegerField(blank=True, null=True, verbose_name='\u52a8\u529b\u7535\u6c60\u7535\u538b')),
                ('current', models.IntegerField(blank=True, null=True, verbose_name='\u52a8\u529b\u7535\u6c60\u7535\u6d41')),
                ('temp', models.IntegerField(blank=True, null=True, verbose_name='\u52a8\u529b\u7535\u6c60\u6e29\u5ea6')),
                ('remain', models.IntegerField(blank=True, null=True, verbose_name='Battery left')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='bus',
            name='bid',
            field=models.CharField(max_length=45, verbose_name='\u6c7d\u8f66\u552f\u4e00\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='bus',
            name='drivers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='\u53f8\u673a'),
        ),
        migrations.AlterField(
            model_name='bus',
            name='plate_number',
            field=models.CharField(max_length=45, verbose_name='\u8f66\u724c\u53f7'),
        ),
        migrations.AlterField(
            model_name='busdata',
            name='failure_info',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u6545\u969c\u4fe1\u606f'),
        ),
        migrations.AlterField(
            model_name='busdata',
            name='gear',
            field=models.IntegerField(blank=True, choices=[(0, 'P'), (1, 'R'), (2, 'N'), (3, 'D')], null=True, verbose_name='\u6863\u4f4d'),
        ),
        migrations.AlterField(
            model_name='busdata',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='\u7eac\u5ea6'),
        ),
        migrations.AlterField(
            model_name='busdata',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='\u7ecf\u5ea6'),
        ),
        migrations.AlterField(
            model_name='busdata',
            name='speed',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u8f66\u901f'),
        ),
        migrations.AlterField(
            model_name='busdata',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, '\u9759\u6b62'), (1, '\u7eaf\u7535\u52a8'), (2, '\u6df7\u5408\u52a8\u529b'), (3, '\u884c\u8f66\u5145\u7535'), (4, '\u5236\u52a8\u56de\u9988')], null=True, verbose_name='\u8f66\u8f86\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='mileagedata',
            name='remain',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u7eed\u9a76\u91cc\u7a0b'),
        ),
        migrations.AlterField(
            model_name='mileagedata',
            name='section',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u5206\u91cc\u7a0b'),
        ),
        migrations.AlterField(
            model_name='mileagedata',
            name='total',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u603b\u91cc\u7a0b'),
        ),
        migrations.AddField(
            model_name='powerbatterydata',
            name='bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Bus'),
        ),
        migrations.AddField(
            model_name='motordata',
            name='bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Bus'),
        ),
        migrations.AddField(
            model_name='gasdata',
            name='bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Bus'),
        ),
        migrations.AddField(
            model_name='fuelcelldata',
            name='bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Bus'),
        ),
        migrations.AddField(
            model_name='energysavingdata',
            name='bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Bus'),
        ),
    ]