# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0003_auto_20150304_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('sex', models.CharField(max_length=4)),
                ('roll_no', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('year_of_registration', models.DateTimeField(verbose_name=b'date published')),
                ('contact_no', models.IntegerField(default=0)),
                ('emailID', models.CharField(max_length=30)),
                ('dept', models.CharField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
