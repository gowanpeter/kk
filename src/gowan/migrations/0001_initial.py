# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('exhibition_name', models.CharField(max_length=45, default='', blank=True)),
                ('exhibition_date', models.DateField(null=True, blank=True)),
                ('exhibition_description', models.CharField(max_length=1000, default='', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('catalogue_id', models.CharField(max_length=45)),
                ('heath_id', models.CharField(max_length=45, blank=True)),
                ('piece_name', models.CharField(max_length=45, blank=True)),
                ('piece_description', models.CharField(max_length=2000, blank=True)),
                ('manufactured_date', models.DateField(null=True, blank=True)),
                ('length_inches', models.IntegerField(null=True, blank=True)),
                ('width_inches', models.IntegerField(null=True, blank=True)),
                ('height_inches', models.IntegerField(null=True, blank=True)),
                ('weight_ounces', models.IntegerField(null=True, blank=True)),
                ('length_mm', models.IntegerField(null=True, blank=True)),
                ('width_mm', models.IntegerField(null=True, blank=True)),
                ('height_mm', models.IntegerField(null=True, blank=True)),
                ('weight_grams', models.IntegerField(null=True, blank=True)),
                ('cataloguer', models.CharField(max_length=45, default='', blank=True)),
                ('catalogue_date', models.DateField(null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('condition', models.ForeignKey(to='gowan.Condition')),
                ('exhibition', models.ForeignKey(to='gowan.Exhibition')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('publication_name', models.CharField(max_length=45, default='', blank=True)),
                ('publication_date', models.DateField(null=True, blank=True)),
                ('publication_author', models.CharField(max_length=45, default='', blank=True)),
                ('publication_media', models.CharField(max_length=45, default='', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='piece',
            name='publication',
            field=models.ForeignKey(to='gowan.Publication'),
            preserve_default=True,
        ),
    ]
