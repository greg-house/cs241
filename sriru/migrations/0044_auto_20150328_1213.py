# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0043_professor_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='CST',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex=b'^\\d{11}$')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='PAN',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]\\{5\\}+[0-9]\\{4\\}+[A-Z]\\{1\\}+$')]),
            preserve_default=True,
        ),
    ]
