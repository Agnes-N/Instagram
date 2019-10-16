# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-16 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_caption', models.CharField(max_length=30)),
                ('pic_image', models.ImageField(null=True, upload_to='images/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
