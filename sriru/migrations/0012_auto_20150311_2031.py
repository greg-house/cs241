# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0011_auto_20150311_2022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project_prof',
            old_name='prof_id',
            new_name='enp_no',
        ),
    ]
