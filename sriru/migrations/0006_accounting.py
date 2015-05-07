# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0005_auto_20150304_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_withdraw', models.DateTimeField(verbose_name=b'date published')),
                ('withdraw_amount', models.IntegerField(default=0)),
                ('proj_id', models.ForeignKey(to='sriru.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
