# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0002_auto_20150301_0716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('agency_no', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('id', models.CharField(max_length=3, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('sex', models.CharField(max_length=4)),
                ('designation', models.CharField(max_length=20)),
                ('enp_no', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('year_of_joining', models.DateTimeField(verbose_name=b'date published')),
                ('contact_no', models.IntegerField(default=0)),
                ('emailID', models.CharField(max_length=30)),
                ('acc_no', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project_Agency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('funding_agency', models.ForeignKey(to='sriru.Agency')),
                ('proj_id', models.ForeignKey(to='sriru.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project_Dept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dept', models.ForeignKey(to='sriru.Department')),
                ('proj_id', models.ForeignKey(to='sriru.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project_Prof',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_investigateor', models.BooleanField(default=False)),
                ('prof_id', models.ForeignKey(to='sriru.Professor')),
                ('proj_id', models.ForeignKey(to='sriru.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.IntegerField(unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
