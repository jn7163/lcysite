# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151030_0635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('body', models.TextField()),
                ('time', models.DateField(verbose_name=django.utils.timezone.now)),
                ('inpassage', models.ForeignKey(to='blog.Passage')),
            ],
        ),
    ]
