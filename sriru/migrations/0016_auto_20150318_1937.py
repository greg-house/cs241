# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0015_auto_20150318_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='project',
        ),
        migrations.RemoveField(
            model_name='student',
            name='project',
        ),
        migrations.AlterField(
            model_name='student',
            name='contact_no',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
