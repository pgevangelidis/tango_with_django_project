# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-24 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20180123_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=' '),
            preserve_default=False,
        ),
    ]
