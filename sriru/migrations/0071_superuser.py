# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0070_auto_20150407_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10)),
                ('password', models.CharField(max_length=30, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
