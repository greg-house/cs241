# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0039_auto_20150326_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='Projects',
        ),
    ]
