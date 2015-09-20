# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityrecord',
            name='activity_datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='activityrecord',
            name='activity_result',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
