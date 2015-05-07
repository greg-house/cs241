# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0050_delete_sex'),
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
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.RemoveField(
            model_name='project',
            name='co_PI',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project',
        ),
        migrations.RemoveField(
            model_name='project_unapproved',
            name='PI',
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
            name='Project_Unapproved',
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
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]
