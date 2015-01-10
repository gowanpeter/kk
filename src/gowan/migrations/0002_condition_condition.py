# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gowan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='condition',
            name='condition',
            field=models.IntegerField(null=True, choices=[(1, 'Pristine'), (2, 'Used, good'), (3, 'Used, worn'), (4, 'Cracked / chipped'), (5, 'Broken')], blank=True),
            preserve_default=True,
        ),
    ]
