# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0052_auto_20150330_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(verbose_name=b'date_of_start(MM/DD/YYYY)'),
            preserve_default=True,
        ),
    ]
