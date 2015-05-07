# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0042_auto_20150326_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='department',
            field=models.ManyToManyField(to='sriru.Department'),
            preserve_default=True,
        ),
    ]
