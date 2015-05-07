# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0004_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='agency_no',
        ),
        migrations.AlterField(
            model_name='agency',
            name='id',
            field=models.IntegerField(unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
