# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0028_auto_20150319_0315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='file_name',
        ),
    ]
