# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0048_auto_20150330_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='sex',
            field=models.CharField(default=b'Male', max_length=5, choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='sex',
            field=models.CharField(default=b'Male', max_length=5, choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='name',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z\\s]+$', message=b'No special characters or Numbers')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z\\s]+$', message=b'No special characters or Numbers')]),
            preserve_default=True,
        ),
    ]
