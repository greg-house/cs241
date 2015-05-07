# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0031_auto_20150319_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='id',
            field=models.AutoField(max_length=3, unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
