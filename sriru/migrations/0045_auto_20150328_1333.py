# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0044_auto_20150328_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_duration',
            name='type_of_purchase',
            field=models.CharField(default=b'NIQ', max_length=5, choices=[(b'NIQ', b'NIQ'), (b'tender', b'Tender')]),
            preserve_default=True,
        ),
    ]
