# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0019_auto_20150318_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='professor',
            name='contact_no',
        ),
        migrations.RemoveField(
            model_name='student',
            name='contact_no',
        ),
        migrations.AddField(
            model_name='professor',
            name='PhoneNo',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^d{10}$', message=b'10 digit mobile number')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='PhoneNo',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^d{10}$', message=b'10 digit mobile number')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='sex',
            field=models.ForeignKey(to='sriru.Sex'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='year_of_joining',
            field=models.DateField(verbose_name=b'Date Joined(MM/DD/YYYY)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='sanction_date',
            field=models.DateField(verbose_name=b'sanction date(MM/DD/YYYY)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(verbose_name=b'date_started(MM/DD/YYYY)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateField(verbose_name=b'Date(MM/DD/YYYY)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase_type',
            name='release_date',
            field=models.DateField(verbose_name=b'released_date(MM/DD/YYYY)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase_type',
            name='result_date',
            field=models.DateField(verbose_name=b'result_date(MM/DD/YYYY)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase_type',
            name='submission_date',
            field=models.DateField(verbose_name=b'last_date(MM/DD/YYYY)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='PhoneNo',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^d{10}$', message=b'10 digit mobile number')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.ForeignKey(to='sriru.Sex'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='year_of_registration',
            field=models.DateField(verbose_name=b'Date Joined(MM/DD/YYYY)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='PhoneNo',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^d{10}$', message=b'10 digit mobile number')]),
            preserve_default=True,
        ),
    ]
