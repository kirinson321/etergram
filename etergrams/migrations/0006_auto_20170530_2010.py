# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etergrams', '0005_auto_20170530_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='photo',
            field=models.ImageField(default='photos/default.jpg', upload_to='photos/'),
        ),
    ]
