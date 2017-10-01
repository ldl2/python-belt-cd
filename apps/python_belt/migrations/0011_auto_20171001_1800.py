# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 18:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('python_belt', '0010_auto_20171001_0612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishes',
            name='who',
        ),
        migrations.AddField(
            model_name='wishes',
            name='fans',
            field=models.ManyToManyField(related_name='favorite', to='python_belt.users'),
        ),
        migrations.AddField(
            model_name='wishes',
            name='whoose',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='wishy', to='python_belt.users'),
            preserve_default=False,
        ),
    ]
