# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-19 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0020_auto_20191019_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=250)),
                ('commented_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.Image')),
                ('posted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.Profile')),
            ],
        ),
    ]
