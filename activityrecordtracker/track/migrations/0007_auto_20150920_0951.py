# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0006_auto_20150920_0936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='feature_result',
            new_name='activity_result',
        ),
    ]
