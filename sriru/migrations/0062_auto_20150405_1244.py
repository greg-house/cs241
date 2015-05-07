# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0061_auto_20150405_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Completed_Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cost', models.PositiveIntegerField(default=0, null=True)),
                ('bill_no', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
                ('date_payment', models.DateField(verbose_name=b'Date of Payment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('name', models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z\\s]+$', message=b'No special characters or Numbers')])),
                ('sex', models.CharField(default=b'Male', max_length=5, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('emp_no', models.CharField(max_length=8, unique=True, serialize=False, primary_key=True, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z]{2}\\d{3}$', message=b'eeXXX')])),
                ('year_of_joining', models.DateField(verbose_name=b'Date Joined(MM/DD/YYYY)')),
                ('contact_no', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10}$', message=b'10 digit mobile number')])),
                ('emailID', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\\.[a-zA-Z0-9.]+$', message=b'Enter valid email id')])),
                ('acc_no', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex=b'^\\d{14,16}$', message=b'14-16 digit account number')])),
                ('password', models.CharField(max_length=30, null=True)),
                ('department', models.ManyToManyField(to='sriru.Department')),
                ('designation', models.ForeignKey(to='sriru.Designation')),
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
                ('duration_of_project', models.IntegerField(default=0)),
                ('updates', models.TextField(null=True)),
                ('approved', models.PositiveIntegerField(default=0)),
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
                ('est_cost', models.PositiveIntegerField(default=0)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('approval', models.PositiveIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchase_duration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_of_purchase', models.CharField(default=b'NIQ', max_length=5, choices=[(b'NIQ', b'NIQ'), (b'tender', b'Tender')])),
                ('release_date', models.DateTimeField(verbose_name=b'released_date')),
                ('submission_date', models.DateTimeField(verbose_name=b'last_date')),
                ('result_date', models.DateTimeField(verbose_name=b'result_date')),
                ('purchase', models.ForeignKey(to='sriru.Purchase')),
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
                ('est_amount', models.PositiveIntegerField(default=0)),
                ('appr_amount', models.PositiveIntegerField(default=0)),
                ('project', models.ForeignKey(to='sriru.Project_Unapproved')),
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
                ('emailID', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\\.[a-zA-Z0-9.]+$', message=b'Enter valid email id')])),
                ('PAN', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]\\{5\\}+[0-9]\\{4\\}+[A-Z]\\{1\\}+$')])),
                ('BankName', models.CharField(max_length=25)),
                ('BankAddress', models.TextField()),
                ('acc_no', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex=b'^\\d{14,16}$', message=b'14-16 digit account number')])),
                ('BranchCode', models.PositiveIntegerField()),
                ('IFSC', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]\\{4\\}')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sanction_ref_no', models.CharField(max_length=10)),
                ('sanction_date', models.DateField(verbose_name=b'sanction date(MM/DD/YYYY)')),
                ('start_date', models.DateTimeField(verbose_name=b'date_of_start(MM/DD/YYYY)')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('co_PI', models.ManyToManyField(related_name='co_investigator', null=True, to='sriru.Professor', blank=True)),
                ('project', models.ForeignKey(to='sriru.Project_Unapproved')),
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
                ('sex', models.CharField(default=b'Male', max_length=6, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('roll_no', models.CharField(max_length=8, unique=True, serialize=False, primary_key=True, validators=[django.core.validators.RegexValidator(regex=b'^\\d{4}[a-zA-Z]{2}\\d{2}$', message=b'1301xxXX')])),
                ('year_of_registration', models.DateField(verbose_name=b'Date Joined(MM/DD/YYYY)')),
                ('contact_no', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10}$', message=b'10 digit mobile number')])),
                ('emailID', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\\.[a-zA-Z0-9.]+$', message=b'Enter valid email id')])),
                ('password', models.CharField(max_length=30, null=True)),
                ('dept', models.ForeignKey(to='sriru.Department')),
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
                ('emailID', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\\.[a-zA-Z0-9.]+$', message=b'Enter valid e-mail ID')])),
                ('ShopActRegNo', models.CharField(max_length=15)),
                ('PAN', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]\\{5\\}+[0-9]\\{4\\}+[A-Z]\\{1\\}+$')])),
                ('CST', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex=b'^\\d{11}$')])),
                ('VAT', models.CharField(max_length=8)),
                ('BankName', models.CharField(max_length=25)),
                ('BankAddress', models.TextField()),
                ('acc_no', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex=b'^\\d{14,16}$', message=b'14-16 digit account number')])),
                ('BranchCode', models.PositiveIntegerField()),
                ('IFSC', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex=b'^[A-Z]\\{4\\}')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='purchase',
            name='sanc_head',
            field=models.ForeignKey(to='sriru.Sanctioned_Head'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payment',
            name='sponsorship',
            field=models.ForeignKey(to='sriru.Sponsorship'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fellowship',
            name='project',
            field=models.ForeignKey(to='sriru.Project_Unapproved'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fellowship',
            name='researcher',
            field=models.ForeignKey(to='sriru.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='completed_purchase',
            name='purchase',
            field=models.ForeignKey(to='sriru.Purchase'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='completed_purchase',
            name='vendor',
            field=models.ForeignKey(to='sriru.Vendor'),
            preserve_default=True,
        ),
    ]
