# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0018_auto_20150318_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='year_of_joining',
            field=models.DateField(verbose_name=b'Date Joined(DDMMYYYY)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='sanction_date',
            field=models.DateField(verbose_name=b'sanction date(DDMMYYYY)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(verbose_name=b'date_started(DDMMYYYY)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateField(verbose_name=b'Date(DDMMYYYY)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase_type',
            name='release_date',
            field=models.DateField(verbose_name=b'released_date(DDMMYYYY)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase_type',
            name='result_date',
            field=models.DateField(verbose_name=b'result_date(DDMMYYYY)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase_type',
            name='submission_date',
            field=models.DateField(verbose_name=b'last_date(DDMMYYYY)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='year_of_registration',
            field=models.DateField(verbose_name=b'Date Joined(DDMMYYYY)'),
            preserve_default=True,
        ),
    ]
