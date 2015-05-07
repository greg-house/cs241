# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0078_messagesponsadmin_messagestudprof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagesponsadmin',
            name='msg_to',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
