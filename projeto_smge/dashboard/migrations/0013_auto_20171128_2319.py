# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20171128_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transdutor',
            name='nome_io12',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
