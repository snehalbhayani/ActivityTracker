# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0005_auto_20150920_0350'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ActivityRecord',
            new_name='Activity',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='activity_name',
            new_name='feature_name',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='activity_result',
            new_name='feature_result',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='parent_activity_name',
            new_name='parent_feature_name',
        ),
    ]
