# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 19:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20170821_1627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='val15seg',
            options={},
        ),
        migrations.RemoveField(
            model_name='administrador',
            name='login',
        ),
        migrations.RemoveField(
            model_name='administrador',
            name='privilegio',
        ),
        migrations.RemoveField(
            model_name='administrador',
            name='senha',
        ),
        migrations.AlterModelTable(
            name='administrador',
            table=None,
        ),
    ]