# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-10 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0002_cinema_siren'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]
