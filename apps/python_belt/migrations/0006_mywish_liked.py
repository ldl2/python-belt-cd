# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_belt', '0005_mywish'),
    ]

    operations = [
        migrations.AddField(
            model_name='mywish',
            name='liked',
            field=models.ManyToManyField(default=False, related_name='wishes', to='python_belt.wishes'),
        ),
    ]
