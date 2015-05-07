# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0056_auto_20150403_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sanction_ref_no', models.CharField(max_length=10)),
                ('sanction_date', models.DateField(verbose_name=b'sanction date(MM/DD/YYYY)')),
                ('duration_of_project', models.IntegerField(default=0)),
                ('start_date', models.DateTimeField(verbose_name=b'date_of_start(MM/DD/YYYY)')),
                ('updates', models.TextField(null=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('PI', models.ForeignKey(related_name='principal_investigator', to='sriru.Professor')),
                ('co_PI', models.ManyToManyField(related_name='co_investigator', null=True, to='sriru.Professor', blank=True)),
                ('project', models.ForeignKey(to='sriru.Project_Unapproved')),
                ('sponsor', models.ForeignKey(to='sriru.Sponsor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
