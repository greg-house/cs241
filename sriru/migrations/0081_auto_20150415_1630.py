# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0080_auto_20150415_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorship',
            name='sanction_ref_no',
            field=models.CharField(unique=True, max_length=10),
            preserve_default=True,
        ),
    ]
