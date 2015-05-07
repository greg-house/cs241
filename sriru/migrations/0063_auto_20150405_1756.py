# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0062_auto_20150405_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='IFSC',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]\\{4\\}+[0-9]\\{7\\}+$')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='IFSC',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]\\{4\\}+[0-9]\\{7\\}+$')]),
            preserve_default=True,
        ),
    ]
