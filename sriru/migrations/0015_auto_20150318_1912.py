# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0014_auto_20150318_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('id', models.CharField(max_length=3, unique=True, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExpenseData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fellowship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pay', models.PositiveIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('date_payment', models.DateTimeField()),
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
                ('emp_no', models.CharField(max_length=8, unique=True, serialize=False, primary_key=True)),
                ('year_of_joining', models.DateField(verbose_name=b'Date Joined')),
                ('contact_no', models.IntegerField(default=0)),
                ('emailID', models.CharField(max_length=30)),
                ('acc_no', models.IntegerField(default=0)),
                ('password', models.CharField(max_length=30, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(max_length=3, unique=True, serialize=False, primary_key=True)),
                ('file_name', models.CharField(max_length=30)),
                ('project_type', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=40)),
                ('sanction_ref_no', models.CharField(max_length=10)),
                ('sanction_date', models.DateTimeField(verbose_name=b'date published')),
                ('duration_of_project', models.IntegerField(default=0)),
                ('start_date', models.DateTimeField(verbose_name=b'date_started')),
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
                ('cost_submitted', models.ForeignKey(to='sriru.ExpenseData')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'Date')),
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
            name='Purchase_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purchase_no', models.PositiveIntegerField()),
                ('type_of_purchase', models.PositiveIntegerField(default=-1, null=True)),
                ('release_date', models.DateTimeField(verbose_name=b'released_date')),
                ('submission_date', models.DateTimeField(verbose_name=b'last_date')),
                ('result_date', models.DateTimeField(verbose_name=b'result_date')),
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
                ('PhoneNo', models.IntegerField(default=0)),
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
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('sex', models.CharField(max_length=4)),
                ('roll_no', models.CharField(max_length=8, unique=True, serialize=False, primary_key=True)),
                ('year_of_registration', models.DateField(verbose_name=b'Date Joined')),
                ('contact_no', models.IntegerField(default=0)),
                ('emailID', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30, null=True)),
                ('dept', models.ForeignKey(to='sriru.Department')),
                ('project', models.ManyToManyField(to='sriru.Project', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('id', models.CharField(max_length=8, unique=True, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=30, null=True)),
                ('Address', models.TextField()),
                ('PhoneNo', models.IntegerField(default=0)),
                ('Email', models.EmailField(max_length=75)),
                ('ShopActRegNo', models.CharField(max_length=15)),
                ('PAN', models.CharField(max_length=10)),
                ('CST', models.CharField(max_length=11)),
                ('VAT', models.CharField(max_length=8)),
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
        migrations.AddField(
            model_name='sponsor',
            name='Projects',
            field=models.ManyToManyField(to='sriru.Project', through='sriru.Sponsorship'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase_type',
            name='others',
            field=models.ManyToManyField(related_name='other_participants', to='sriru.Vendor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase_type',
            name='vendor',
            field=models.ForeignKey(related_name='winner', to='sriru.Vendor'),
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
            model_name='professor',
            name='project',
            field=models.ManyToManyField(to='sriru.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fellowship',
            name='researcher',
            field=models.ForeignKey(to='sriru.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='expensedata',
            name='sanctioned_head',
            field=models.ManyToManyField(to='sriru.Sanctioned_Head'),
            preserve_default=True,
        ),
    ]
