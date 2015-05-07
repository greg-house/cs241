# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0047_auto_20150330_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='student',
            name='sex',
        ),
        migrations.AlterField(
            model_name='professor',
            name='name',
            field=models.CharField(default=b'Male', max_length=5, choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default=b'Male', max_length=5, choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
            preserve_default=True,
        ),
    ]
