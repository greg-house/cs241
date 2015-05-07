# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0081_auto_20150415_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorship',
            name='sanction_ref_no',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
