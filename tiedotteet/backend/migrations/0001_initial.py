# Generated by Django 2.1 on 2019-06-21 17:50

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('order', models.IntegerField(blank=True, default=0, null=True)),
                ('login_required', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MailConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(default='mail.aalto.fi', max_length=50)),
                ('port', models.CharField(default='587', max_length=10)),
                ('username', models.CharField(default='tiedottaja@aalto.fi', max_length=50)),
                ('password', models.CharField(default='salasana', max_length=50)),
                ('use_tls', models.BooleanField(default=True)),
                ('fail_silently', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=datetime.date(2019, 6, 28))),
                ('deadline_date', models.DateField(blank=True, default=datetime.date(2019, 6, 28), null=True)),
                ('show_deadline', models.BooleanField(default=False)),
                ('visible', models.BooleanField(default=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='backend.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='messages', to='backend.Tag'),
        ),
    ]