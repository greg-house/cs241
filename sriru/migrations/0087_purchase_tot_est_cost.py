# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0086_auto_20150415_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='tot_est_cost',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
