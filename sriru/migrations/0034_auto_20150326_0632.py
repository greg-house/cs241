# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0033_auto_20150326_0412'),
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
            name='Designation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
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
                ('name', models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z\\s]+$', message=b'No special characters or Numbers')])),
                ('emp_no', models.CharField(max_length=8, unique=True, serialize=False, primary_key=True, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z]{2}\\d{3}$', message=b'eeXXX')])),
                ('year_of_joining', models.DateField(verbose_name=b'Date Joined(MM/DD/YYYY)')),
                ('contact_no', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10}$', message=b'10 digit mobile number')])),
                ('emailID', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\\.[a-zA-Z0-9.]+$', message=b'10 digit mobile number or 11 digit landline number')])),
                ('acc_no', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex=b'^\\d{14-16}$', message=b'14-16 digit account number')])),
                ('password', models.CharField(max_length=30, null=True)),
                ('designation', models.ForeignKey(to='sriru.Designation')),
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
                ('updates', models.TextField(null=True)),
                ('PI', models.ForeignKey(related_name='principal_investigator', to='sriru.Professor')),
                ('co_PI', models.ManyToManyField(related_name='co_investigator', null=True, to='sriru.Professor')),
                ('fellowship', models.ManyToManyField(to='sriru.Fellowship', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project_Unapproved',
            fields=[
                ('id', models.AutoField(max_length=3, unique=True, serialize=False, primary_key=True)),
                ('project_type', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=40)),
                ('approved', models.BooleanField(default=False)),
                ('PI', models.ForeignKey(to='sriru.Professor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'date published')),
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
                ('project', models.ForeignKey(to='sriru.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('name', models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z\\s]+$', message=b'No special characters or Numbers')])),
                ('id', models.AutoField(max_length=3, unique=True, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=30, null=True)),
                ('Address', models.TextField()),
                ('PhoneNo', models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10}$', message=b'10 digit mobile number')])),
                ('emailID', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\\.[a-zA-Z0-9.]+$', message=b'10 digit mobile number or 11 digit landline number')])),
                ('PAN', models.CharField(max_length=10)),
                ('BankName', models.CharField(max_length=25)),
                ('BankAddress', models.TextField()),
                ('acc_no', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex=b'^\\d{14-16}$', message=b'14-16 digit account number')])),
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
                ('name', models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z\\s]+$', message=b'No special characters or Numbers')])),
                ('roll_no', models.CharField(max_length=8, unique=True, serialize=False, primary_key=True, validators=[django.core.validators.RegexValidator(regex=b'^\\d{4}[a-zA-Z]{2}\\d{4}$', message=b'1301xxXX')])),
                ('year_of_registration', models.DateField(verbose_name=b'Date Joined(MM/DD/YYYY)')),
                ('contact_no', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10}$', message=b'10 digit mobile number')])),
                ('emailID', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\\.[a-zA-Z0-9.]+$', message=b'10 digit mobile number or 11 digit landline number')])),
                ('password', models.CharField(max_length=30, null=True)),
                ('dept', models.ForeignKey(to='sriru.Department')),
                ('sex', models.ForeignKey(to='sriru.Sex')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('name', models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z\\s]+$', message=b'No special characters or Numbers')])),
                ('id', models.AutoField(max_length=4, unique=True, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=30, null=True)),
                ('Address', models.TextField()),
                ('PhoneNo', models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10,11}$', message=b'10 digit mobile number or 11 digit landline number')])),
                ('emailID', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\\.[a-zA-Z0-9.]+$', message=b'10 digit mobile number or 11 digit landline number')])),
                ('ShopActRegNo', models.CharField(max_length=15)),
                ('PAN', models.CharField(max_length=10)),
                ('CST', models.CharField(max_length=11)),
                ('VAT', models.CharField(max_length=8)),
                ('BankName', models.CharField(max_length=25)),
                ('BankAddress', models.TextField()),
                ('acc_no', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex=b'^\\d{14-16}$', message=b'14-16 digit account number')])),
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
            model_name='professor',
            name='sex',
            field=models.ForeignKey(to='sriru.Sex'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fellowship',
            name='researcher',
            field=models.ForeignKey(to='sriru.Student'),
            preserve_default=True,
        ),
    ]
