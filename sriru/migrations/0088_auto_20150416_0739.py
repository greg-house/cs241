# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0087_purchase_tot_est_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='sex',
            field=models.CharField(default=b'Male', max_length=6, choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
            preserve_default=True,
        ),
    ]
