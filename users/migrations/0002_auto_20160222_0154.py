# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 01:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='collaborators',
        ),
        migrations.RemoveField(
            model_name='task',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
