# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0077_auto_20150412_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageSponsAdmin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('msg', models.TextField()),
                ('seen', models.BooleanField(default=False)),
                ('msg_from', models.ForeignKey(to='sriru.Sponsor')),
                ('msg_to', models.ForeignKey(to='sriru.SuperUser')),
                ('project', models.ForeignKey(to='sriru.Project_Unapproved')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MessageStudProf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('msg', models.TextField()),
                ('seen', models.BooleanField(default=False)),
                ('msg_from', models.ForeignKey(to='sriru.Student')),
                ('msg_to', models.ForeignKey(to='sriru.Professor')),
                ('project', models.ForeignKey(to='sriru.Project_Unapproved')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
