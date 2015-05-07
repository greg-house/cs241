# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0030_auto_20150319_0411'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(max_length=3, unique=True, serialize=False, primary_key=True)),
                ('project_type', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=40)),
                ('sanction_ref_no', models.CharField(max_length=10)),
                ('sanction_date', models.DateField(verbose_name=b'sanction date(MM/DD/YYYY)')),
                ('duration_of_project', models.IntegerField(default=0)),
                ('start_date', models.DateTimeField(verbose_name=b'date_started(MM/DD/YYYY)')),
                ('update', models.TextField(null=True)),
                ('PI', models.ForeignKey(related_name='principal_investigator', to='sriru.Professor')),
                ('co_PI', models.ManyToManyField(related_name='co_investigator', null=True, to='sriru.Professor')),
                ('cost_submitted', models.ForeignKey(related_name='expected_cost', to='sriru.ExpenseData', null=True)),
                ('fellowship', models.ManyToManyField(to='sriru.Fellowship', null=True)),
                ('payment', models.ManyToManyField(to='sriru.Payment', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project_Unapproved',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_type', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=40)),
                ('approved', models.BooleanField(default=0)),
                ('PI', models.ForeignKey(to='sriru.Professor')),
                ('cost_submitted', models.ForeignKey(to='sriru.ExpenseData', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'Date(MM/DD/YYYY)')),
                ('prod_title', models.CharField(max_length=50)),
                ('prod_spec', models.TextField()),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('purchase_no', models.PositiveIntegerField(null=True)),
                ('approval', models.PositiveIntegerField(default=0)),
                ('cost', models.PositiveIntegerField(default=0, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sanctioned_Head',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('amount', models.PositiveIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('id', models.CharField(max_length=8, unique=True, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=30, null=True)),
                ('Address', models.TextField()),
                ('PhoneNo', models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10,11}$', message=b'10 digit mobile number or 11 digit landline number')])),
                ('Email', models.EmailField(max_length=75)),
                ('PAN', models.CharField(max_length=10)),
                ('BankName', models.CharField(max_length=25)),
                ('BankAddress', models.TextField()),
                ('AccountNo', models.CharField(max_length=15)),
                ('BranchCode', models.PositiveIntegerField()),
                ('IFSC', models.CharField(max_length=11)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('project', models.ForeignKey(to='sriru.Project')),
                ('sponsor', models.ForeignKey(to='sriru.Sponsor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='Projects',
            field=models.ManyToManyField(to='sriru.Project', through='sriru.Sponsorship'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='est_cost',
            field=models.ForeignKey(related_name='cost_estimated', to='sriru.Sanctioned_Head'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='sanctioned_cost',
            field=models.ForeignKey(related_name='cost_sponsored', to='sriru.Sanctioned_Head', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='vendor',
            field=models.ForeignKey(to='sriru.Vendor', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='purchase',
            field=models.ManyToManyField(to='sriru.Purchase', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='sanction_limit',
            field=models.ForeignKey(to='sriru.ExpenseData', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='expensedata',
            name='sanctioned_head',
            field=models.ManyToManyField(to='sriru.Sanctioned_Head'),
            preserve_default=True,
        ),
    ]
