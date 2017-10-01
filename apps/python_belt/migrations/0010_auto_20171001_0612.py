# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 06:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('python_belt', '0009_auto_20171001_0610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='liked',
        ),
        migrations.AddField(
            model_name='favorite',
            name='liked',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='wishes', to='python_belt.wishes'),
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='likes',
        ),
        migrations.AddField(
            model_name='favorite',
            name='likes',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='washy', to='python_belt.users'),
        ),
        migrations.RemoveField(
            model_name='wishes',
            name='who',
        ),
        migrations.AddField(
            model_name='wishes',
            name='who',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='wishy', to='python_belt.users'),
        ),
    ]