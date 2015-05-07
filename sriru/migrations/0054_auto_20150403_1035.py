# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0053_auto_20150403_1000'),
    ]

    operations = [
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
            name='project',
        ),
        migrations.RemoveField(
            model_name='sponsorship',
            name='project',
        ),
        migrations.RemoveField(
            model_name='sponsorship',
            name='sponsor',
        ),
        migrations.DeleteModel(
            name='Sponsorship',
        ),
        migrations.AlterField(
            model_name='fellowship',
            name='project',
            field=models.ForeignKey(to='sriru.Project_Unapproved'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
