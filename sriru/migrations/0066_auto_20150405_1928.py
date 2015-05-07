# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0065_auto_20150405_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_unapproved',
            name='duration_of_project',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
