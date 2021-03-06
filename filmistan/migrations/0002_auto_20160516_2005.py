# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-16 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import filmistan.models


class Migration(migrations.Migration):

    dependencies = [
        ('filmistan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('username', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='youremail@example.com', max_length=50)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=filmistan.models.get_image_path_2)),
            ],
        ),
        migrations.RemoveField(
            model_name='film',
            name='rating',
        ),
        migrations.AddField(
            model_name='film',
            name='description',
            field=models.CharField(default='Film Özeti', max_length=1000),
        ),
        migrations.AddField(
            model_name='film',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=filmistan.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='actor',
            name='birthDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='birthDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='director',
            name='surname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.RemoveField(
            model_name='film',
            name='director',
        ),
        migrations.AddField(
            model_name='film',
            name='director',
            field=models.ManyToManyField(to='filmistan.Director'),
        ),
        migrations.RemoveField(
            model_name='film',
            name='genre',
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(to='filmistan.Genre'),
        ),
        migrations.AlterField(
            model_name='year',
            name='yy',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
        migrations.AddField(
            model_name='film',
            name='youtube_trailer',
            field=models.ManyToManyField(to='filmistan.Trailer'),
        ),
    ]
