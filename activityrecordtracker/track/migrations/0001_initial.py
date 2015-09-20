# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity_name', models.CharField(max_length=20)),
                ('parent_activity_name', models.CharField(max_length=20, blank=True)),
                ('activity_result', models.CharField(default=b'I', max_length=1, blank=True, choices=[(b'S', b'Success'), (b'F', b'Failure'), (b'E', b'Error'), (b'I', b'In Progress')])),
                ('username', models.CharField(max_length=20, blank=True)),
                ('activity_datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'get_latest_by': 'activity_datetime',
                'verbose_name': 'Activity Record',
            },
        ),
    ]
