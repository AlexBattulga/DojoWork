# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-21 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='full_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='DEFUALT VALUE', max_length=255),
        ),
    ]
