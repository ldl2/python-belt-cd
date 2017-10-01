# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_belt', '0007_auto_20171001_0453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='liked',
        ),
        migrations.AddField(
            model_name='favorite',
            name='liked',
            field=models.ManyToManyField(default=False, related_name='wishes', to='python_belt.wishes'),
        ),
    ]
