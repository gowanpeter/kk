# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gowan', '0004_auto_20150110_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conditionchoice',
            name='name',
        ),
    ]
