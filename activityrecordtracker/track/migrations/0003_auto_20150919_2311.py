# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0002_auto_20150919_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityrecord',
            name='parent_activity_name',
            field=models.CharField(default=b'I', max_length=20, blank=True, choices=[(b'S', b'Success'), (b'F', b'Failure'), (b'E', b'Error'), (b'I', b'In Progress')]),
        ),
    ]
