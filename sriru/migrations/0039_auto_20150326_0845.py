# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0038_auto_20150326_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='co_PI',
            field=models.ManyToManyField(related_name='co_investigator', null=True, to='sriru.Professor', blank=True),
            preserve_default=True,
        ),
    ]
