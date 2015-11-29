# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Auther',
            new_name='Author',
        ),
        migrations.RenameField(
            model_name='passage',
            old_name='auther',
            new_name='author',
        ),
    ]
