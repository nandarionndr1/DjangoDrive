# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-03 03:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0003_auto_20180103_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='uploadDate',
            field=models.DateTimeField(auto_created=True, blank=True, default=datetime.datetime.now),
        ),
    ]
