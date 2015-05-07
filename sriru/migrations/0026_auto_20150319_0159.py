# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0025_auto_20150319_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='designation',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
    ]
