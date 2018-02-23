# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-23 13:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20180223_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='Image_Category',
            field=models.ManyToManyField(blank=True, to='photos.Category'),
        ),
        migrations.AddField(
            model_name='image',
            name='Image_Location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.Location'),
        ),
    ]
