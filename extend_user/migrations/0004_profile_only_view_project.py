# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-16 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extend_user', '0003_auto_20171222_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='only_view_project',
            field=models.BooleanField(default=False),
        ),
    ]
