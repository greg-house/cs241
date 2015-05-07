# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0010_auto_20150311_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'date published')),
                ('prod_spec', models.CharField(max_length=40)),
                ('quantity', models.IntegerField(default=1)),
                ('total_cost', models.IntegerField(default=0)),
                ('proj', models.ForeignKey(to='sriru.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
