# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sriru', '0055_sponsorship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsorship',
            name='PI',
        ),
        migrations.RemoveField(
            model_name='sponsorship',
            name='co_PI',
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
    ]
