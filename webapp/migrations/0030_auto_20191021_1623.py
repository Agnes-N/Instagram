# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-21 14:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0029_auto_20191021_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='posted_by',
        ),
        migrations.RemoveField(
            model_name='followers',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
