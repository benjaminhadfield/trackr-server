# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0006_auto_20171006_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='charge_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]