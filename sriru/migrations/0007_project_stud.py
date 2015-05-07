# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0006_accounting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Stud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proj_id', models.ForeignKey(to='sriru.Project')),
                ('roll_no', models.ForeignKey(to='sriru.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
