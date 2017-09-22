# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 13:21
from __future__ import unicode_literals

import dashboard.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=True, verbose_name='staff')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='dashboard/static/avatars/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', dashboard.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Classificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente_has_concessionaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Coleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_instalacao', models.DateTimeField(verbose_name='data')),
                ('hora_instalacao', models.DateTimeField(verbose_name='hora')),
                ('saida1', models.CharField(max_length=255)),
                ('saida2', models.CharField(max_length=255)),
                ('saida3', models.CharField(max_length=255)),
                ('saida4', models.CharField(max_length=255)),
                ('saida5', models.CharField(max_length=255)),
                ('saida6', models.CharField(max_length=255)),
                ('saida7', models.CharField(max_length=255)),
                ('saida8', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Concessionaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('hp_inicio', models.DateTimeField(verbose_name='hp inicio')),
                ('hp_fim', models.DateTimeField(verbose_name='hp fim')),
            ],
        ),
        migrations.CreateModel(
            name='Constante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('valor', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Conta_contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conta_contrato', models.CharField(max_length=255)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Imposto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('valor', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('valor', models.CharField(max_length=255)),
                ('id_classificacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Classificacao')),
            ],
        ),
        migrations.CreateModel(
            name='Transdutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_instalacao', models.DateTimeField(verbose_name='Data instalacao')),
                ('numero_serie', models.CharField(max_length=255)),
                ('id_classificacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Classificacao')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='coleta',
            name='id_transdutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Transdutor'),
        ),
        migrations.AddField(
            model_name='cliente_has_concessionaria',
            name='id_concessionaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Concessionaria'),
        ),
        migrations.AddField(
            model_name='classificacao',
            name='id_concessionaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Concessionaria'),
        ),
    ]
