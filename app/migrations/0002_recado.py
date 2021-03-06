# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-06 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=300)),
                ('foto', models.TextField(blank=True, null=True)),
                ('texto', models.TextField()),
                ('aprovado', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Recado',
                'verbose_name_plural': 'Recados',
            },
        ),
    ]
