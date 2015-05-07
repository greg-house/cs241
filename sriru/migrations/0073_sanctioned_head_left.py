# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0072_sanctioned_head_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanctioned_head',
            name='left',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
