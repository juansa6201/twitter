# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-10 05:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retweet',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_retuits', to='twitter.Tweet'),
        ),
    ]