# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0013_auto_20150312_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounting',
            name='proj_id',
        ),
        migrations.DeleteModel(
            name='Accounting',
        ),
        migrations.RemoveField(
            model_name='project_agency',
            name='funding_agency',
        ),
        migrations.DeleteModel(
            name='Agency',
        ),
        migrations.RemoveField(
            model_name='project_agency',
            name='proj_id',
        ),
        migrations.DeleteModel(
            name='Project_Agency',
        ),
        migrations.RemoveField(
            model_name='project_dept',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='project_dept',
            name='proj_id',
        ),
        migrations.DeleteModel(
            name='Project_Dept',
        ),
        migrations.RemoveField(
            model_name='project_prof',
            name='enp_no',
        ),
        migrations.DeleteModel(
            name='Professor',
        ),
        migrations.RemoveField(
            model_name='project_prof',
            name='proj_id',
        ),
        migrations.DeleteModel(
            name='Project_Prof',
        ),
        migrations.RemoveField(
            model_name='project_stud',
            name='proj_id',
        ),
        migrations.RemoveField(
            model_name='project_stud',
            name='roll_no',
        ),
        migrations.DeleteModel(
            name='Project_Stud',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='proj',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Purchase',
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
    ]
