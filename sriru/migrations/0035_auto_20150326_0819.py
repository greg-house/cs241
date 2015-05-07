# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0034_auto_20150326_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(max_length=8, unique=True, serialize=False, primary_key=True, validators=[django.core.validators.RegexValidator(regex=b'^\\d{4}[a-zA-Z]{2}\\d{2}$', message=b'1301xxXX')]),
            preserve_default=True,
        ),
    ]
