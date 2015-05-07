# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('project_no', models.IntegerField(default=0)),
                ('file_name', models.CharField(max_length=30)),
                ('project_type', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=40)),
                ('sanction_ref_no', models.IntegerField(max_length=10)),
                ('sanction_date', models.DateTimeField(verbose_name=b'date published')),
                ('duration_of_project', models.IntegerField(default=0)),
                ('start_date', models.DateTimeField(verbose_name=b'date published')),
                ('cost_submitted', models.IntegerField(default=0)),
                ('sanction_limit', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
