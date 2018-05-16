# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-13 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_kulukorvaus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kulukorvaus',
            name='sum_euros',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Summa (euroa)'),
        ),
    ]
