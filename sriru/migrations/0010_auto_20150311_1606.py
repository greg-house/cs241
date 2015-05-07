# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0009_auto_20150310_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='id',
            field=models.CharField(max_length=8, unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(max_length=3, unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='enp_no',
            field=models.CharField(max_length=8, unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(max_length=8, unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
