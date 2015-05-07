# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0021_auto_20150319_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='PhoneNo',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^\\d{9,10}$', message=b'10 digit mobile number')]),
            preserve_default=True,
        ),
    ]
