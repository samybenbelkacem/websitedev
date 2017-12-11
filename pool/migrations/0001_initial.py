# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-10 16:14
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('adress', models.CharField(max_length=60)),
                ('zip_code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
                ('nbr_rooms', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2100)])),
                ('overview', models.TextField(max_length=3000)),
                ('trailer_url', models.URLField(verbose_name=b'Link to the trailer')),
                ('language', models.CharField(max_length=60)),
                ('poster', models.ImageField(upload_to=b'')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Showing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pool.Cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pool.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='VoteMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pool.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VoteShowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('showing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pool.Showing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='sales',
            name='showing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pool.Showing'),
        ),
        migrations.AddField(
            model_name='sales',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]