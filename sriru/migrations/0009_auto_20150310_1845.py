# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0008_auto_20150310_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='password',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='password',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
    ]
