# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-13 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_poytakirjat', '0006_auto_20180419_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='dokumentti',
            name='gdrive_id',
            field=models.CharField(default='9999999999999999999999999', max_length=99),
            preserve_default=False,
        ),
    ]