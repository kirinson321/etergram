# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etergrams', '0002_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='photo',
            field=models.ImageField(default='/home/marcin/Desktop/python/projects/etergram/media/photos/default.jpg', upload_to='photos/'),
        ),
    ]