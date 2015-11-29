# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auther',
            fields=[
                ('name', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('brithday', models.DateField(blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Passage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('time', models.DateField(verbose_name=django.utils.timezone.now)),
                ('auther', models.ForeignKey(blank=True, to='blog.Auther', null=True)),
            ],
        ),
    ]
