# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0026_auto_20150319_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_unapproved',
            name='cost_submitted',
            field=models.ForeignKey(to='sriru.ExpenseData', null=True),
            preserve_default=True,
        ),
    ]
