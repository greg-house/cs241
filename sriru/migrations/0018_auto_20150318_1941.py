# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0017_auto_20150318_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='acc_no',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='emailID',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='sanction_date',
            field=models.DateField(verbose_name=b'sanction date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateField(verbose_name=b'Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase_type',
            name='release_date',
            field=models.DateField(verbose_name=b'released_date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase_type',
            name='result_date',
            field=models.DateField(verbose_name=b'result_date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase_type',
            name='submission_date',
            field=models.DateField(verbose_name=b'last_date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='PhoneNo',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='emailID',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='PhoneNo',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
