# Generated by Django 2.1 on 2019-06-21 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='mailconfiguration',
            options={'verbose_name': 'mailikonfiguraatio', 'verbose_name_plural': 'Mailikonfiguraatiot'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'tiedote', 'verbose_name_plural': 'Tiedotteet'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'tagi', 'verbose_name_plural': 'Tagit'},
        ),
    ]
