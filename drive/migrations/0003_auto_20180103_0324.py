# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-03 03:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0002_auto_20171230_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='filedir',
            field=models.ImageField(default=b'pics/default.jpeg', upload_to=b'pics/'),
        ),
        migrations.AlterField(
            model_name='file',
            name='parent_folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drive.Folder'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='foldername',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
