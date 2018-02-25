# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-25 05:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_auto_20180223_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='Image_Category',
        ),
        migrations.AddField(
            model_name='image',
            name='Image_Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.Category'),
        ),
    ]