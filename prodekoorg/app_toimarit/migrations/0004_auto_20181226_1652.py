# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-26 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_toimarit', '0003_auto_20181226_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hallituksenjasen',
            name='firstname',
            field=models.CharField(max_length=30, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='hallituksenjasen',
            name='lastname',
            field=models.CharField(max_length=30, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='toimari',
            name='firstname',
            field=models.CharField(max_length=30, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='toimari',
            name='lastname',
            field=models.CharField(max_length=30, verbose_name='Last Name'),
        ),
    ]