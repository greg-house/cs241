# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0012_auto_20150311_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dept',
            field=models.ForeignKey(to='sriru.Department'),
            preserve_default=True,
        ),
    ]
