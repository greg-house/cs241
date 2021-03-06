# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0084_auto_20150415_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completed_purchase',
            name='purchase',
        ),
        migrations.RemoveField(
            model_name='completed_purchase',
            name='vendor',
        ),
        migrations.DeleteModel(
            name='Completed_Purchase',
        ),
        migrations.RemoveField(
            model_name='fellowship',
            name='project',
        ),
        migrations.RemoveField(
            model_name='fellowship',
            name='researcher',
        ),
        migrations.DeleteModel(
            name='Fellowship',
        ),
        migrations.RemoveField(
            model_name='messagesponsadmin',
            name='msg_from',
        ),
        migrations.RemoveField(
            model_name='messagesponsadmin',
            name='project',
        ),
        migrations.DeleteModel(
            name='MessageSponsAdmin',
        ),
        migrations.RemoveField(
            model_name='messagestudprof',
            name='msg_from',
        ),
        migrations.RemoveField(
            model_name='messagestudprof',
            name='msg_to',
        ),
        migrations.RemoveField(
            model_name='messagestudprof',
            name='project',
        ),
        migrations.DeleteModel(
            name='MessageStudProf',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='sponsorship',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='department',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='designation',
        ),
        migrations.DeleteModel(
            name='Designation',
        ),
        migrations.RemoveField(
            model_name='project_unapproved',
            name='PI',
        ),
        migrations.RemoveField(
            model_name='project_unapproved',
            name='co_PI',
        ),
        migrations.DeleteModel(
            name='Professor',
        ),
        migrations.RemoveField(
            model_name='project_unapproved',
            name='department',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='sanc_head',
        ),
        migrations.RemoveField(
            model_name='purchase_duration',
            name='purchase',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
        migrations.DeleteModel(
            name='Purchase_duration',
        ),
        migrations.RemoveField(
            model_name='sanctioned_head',
            name='project',
        ),
        migrations.DeleteModel(
            name='Sanctioned_Head',
        ),
        migrations.RemoveField(
            model_name='sponsorship',
            name='project',
        ),
        migrations.DeleteModel(
            name='Project_Unapproved',
        ),
        migrations.RemoveField(
            model_name='sponsorship',
            name='sponsor',
        ),
        migrations.DeleteModel(
            name='Sponsor',
        ),
        migrations.DeleteModel(
            name='Sponsorship',
        ),
        migrations.RemoveField(
            model_name='student',
            name='dept',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='SuperUser',
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]
