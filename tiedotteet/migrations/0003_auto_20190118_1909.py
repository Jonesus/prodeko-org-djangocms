# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-18 19:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiedotteet', '0002_auto_20181229_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='deadline_date',
            field=models.DateField(blank=True, default=datetime.date(2019, 1, 25), null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='end_date',
            field=models.DateField(default=datetime.date(2019, 1, 25)),
        ),
    ]