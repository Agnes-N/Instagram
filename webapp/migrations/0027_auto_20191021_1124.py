# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-21 09:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0026_auto_20191020_1513'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='preference',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='preference',
            name='post',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='user',
        ),
        migrations.RemoveField(
            model_name='followers',
            name='to_user',
        ),
        migrations.RemoveField(
            model_name='image',
            name='dislikes',
        ),
        migrations.AddField(
            model_name='followers',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.Profile'),
        ),
        migrations.AlterField(
            model_name='followers',
            name='from_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Preference',
        ),
    ]
