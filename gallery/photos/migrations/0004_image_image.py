# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-23 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20180223_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='Image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
