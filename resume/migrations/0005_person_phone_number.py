# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_resume_objective'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='phone_number',
            field=models.CharField(default=3014129718, max_length=10),
            preserve_default=False,
        ),
    ]