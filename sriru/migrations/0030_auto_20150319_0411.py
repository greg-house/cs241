# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0029_remove_project_file_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expensedata',
            name='sanctioned_head',
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
            name='cost_submitted',
        ),
        migrations.RemoveField(
            model_name='project',
            name='fellowship',
        ),
        migrations.RemoveField(
            model_name='project',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='project',
            name='purchase',
        ),
        migrations.RemoveField(
            model_name='project',
            name='sanction_limit',
        ),
        migrations.DeleteModel(
            name='ExpenseData',
        ),
        migrations.RemoveField(
            model_name='project_unapproved',
            name='PI',
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
        migrations.DeleteModel(
            name='Sanctioned_Head',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='Projects',
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
    ]
