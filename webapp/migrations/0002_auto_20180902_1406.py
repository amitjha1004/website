# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-02 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='id',
        ),
        migrations.AlterField(
            model_name='employees',
            name='emp_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
