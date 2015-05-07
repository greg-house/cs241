# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0073_sanctioned_head_left'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fellowship',
            name='project',
        ),
        migrations.RemoveField(
            model_name='fellowship',
            name='researcher',
        ),
        migrations.DeleteModel(
            name='Fellowship',
        ),
    ]
