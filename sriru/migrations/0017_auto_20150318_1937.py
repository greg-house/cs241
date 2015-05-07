# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0016_auto_20150318_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='contact_no',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
