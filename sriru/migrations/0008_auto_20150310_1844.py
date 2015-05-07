# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0007_project_stud'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='password',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='professor',
            name='password',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
