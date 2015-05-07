# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0074_auto_20150408_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fellowship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pay', models.PositiveIntegerField(default=0)),
                ('project', models.ForeignKey(to='sriru.Project_Unapproved')),
                ('researcher', models.ForeignKey(to='sriru.Student')),
                ('sanc_head', models.ForeignKey(to='sriru.Sanctioned_Head')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
