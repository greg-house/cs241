# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0079_auto_20150415_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='acc_no',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10,16}$', message=b'10-16 digit account number')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(verbose_name=b'Date(MM/DD/YYYY)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='IFSC',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]{4}\\d{7}$', message=b'Format: aaaa999999')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='PAN',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]{5}\\d{4}[A-Za-z]{1}$', message=b'Format: aaaaa9999a')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='acc_no',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10,16}$', message=b'10-16 digit account number')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='CST',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex=b'^\\d{11}$', message=b'11 digit only')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='IFSC',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]{4}\\d{7}$', message=b'Format: aaaa999999')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='PAN',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]{5}\\d{4}[A-Z]{1}$', message=b'Format: aaaaa9999a')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='acc_no',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10,16}$', message=b'10-16 digit account number')]),
            preserve_default=True,
        ),
    ]
