# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-19 16:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0019_auto_20191019_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='commented_image',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='posted_by',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
