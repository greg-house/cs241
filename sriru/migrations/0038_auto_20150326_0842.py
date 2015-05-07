# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0037_auto_20150326_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='acc_no',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex=b'^\\d{14,16}$', message=b'14-16 digit account number')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='emailID',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\\.[a-zA-Z0-9.]+$', message=b'Enter valid email id')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='emailID',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\\.[a-zA-Z0-9.]+$', message=b'Enter valid email id')]),
            preserve_default=True,
        ),
    ]
