# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0040_remove_sponsor_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fellowship',
            name='researcher',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='designation',
        ),
        migrations.DeleteModel(
            name='Designation',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='project',
            name='PI',
        ),
        migrations.RemoveField(
            model_name='project',
            name='co_PI',
        ),
        migrations.RemoveField(
            model_name='project',
            name='fellowship',
        ),
        migrations.DeleteModel(
            name='Fellowship',
        ),
        migrations.RemoveField(
            model_name='project_unapproved',
            name='PI',
        ),
        migrations.DeleteModel(
            name='Professor',
        ),
        migrations.DeleteModel(
            name='Project_Unapproved',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='est_cost',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='sanctioned_cost',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='vendor',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
        migrations.RemoveField(
            model_name='purchase_type',
            name='others',
        ),
        migrations.RemoveField(
            model_name='purchase_type',
            name='vendor',
        ),
        migrations.DeleteModel(
            name='Purchase_Type',
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
            name='Project',
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
        migrations.RemoveField(
            model_name='student',
            name='sex',
        ),
        migrations.DeleteModel(
            name='Sex',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]
