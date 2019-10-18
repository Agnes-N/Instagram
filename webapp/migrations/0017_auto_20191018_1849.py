# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-18 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_image_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='commented_image',
        ),
        migrations.AlterField(
            model_name='comments',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.Profile'),
        ),
    ]
