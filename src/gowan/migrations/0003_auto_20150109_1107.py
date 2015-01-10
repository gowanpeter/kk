# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gowan', '0002_condition_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='condition',
            field=models.IntegerField(choices=[(1, 'Pristine'), (2, 'Used, good'), (3, 'Used, worn'), (4, 'Cracked / chipped'), (5, 'Broken')], blank=True, null=True, default=2),
            preserve_default=True,
        ),
    ]
