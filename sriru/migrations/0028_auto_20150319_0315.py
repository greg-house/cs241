# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0027_auto_20150319_0219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_unapproved',
            name='cost_submitted',
        ),
        migrations.AlterField(
            model_name='professor',
            name='PhoneNo',
            field=models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10,11}$', message=b'10 digit mobile number or 11 digit landline number')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='PhoneNo',
            field=models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10,11}$', message=b'10 digit mobile number or 11 digit landline number')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='PhoneNo',
            field=models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10,11}$', message=b'10 digit mobile number or 11 digit landline number')]),
            preserve_default=True,
        ),
    ]
