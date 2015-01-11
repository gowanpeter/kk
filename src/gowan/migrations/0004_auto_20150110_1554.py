# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gowan', '0003_auto_20150109_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConditionChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('condition', models.CharField(max_length=1, choices=[('a', 'Pristine'), ('b', 'Used, good'), ('c', 'Used, worn'), ('d', 'Cracked / chipped'), ('e', 'Broken')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('documentation_name', models.CharField(blank=True, max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='documentation_link_piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('documentation_date', models.DateField(blank=True, null=True)),
                ('documentation_author', models.CharField(blank=True, max_length=45)),
                ('documentation_media', models.CharField(blank=True, max_length=45)),
                ('documentation_location', models.CharField(blank=True, max_length=45)),
                ('documentation', models.ForeignKey(to='gowan.Documentation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='glaze_link_piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GlazeLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('glaze_name', models.CharField(blank=True, max_length=45)),
                ('glaze_description', models.CharField(blank=True, max_length=500)),
                ('glaze_begin_date', models.DateField(blank=True, null=True)),
                ('glaze_end_date', models.DateField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='heath_line_link_piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HeathLineLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('heath_line_name', models.CharField(blank=True, max_length=45)),
                ('heath_line_begin_date', models.DateField(blank=True, null=True)),
                ('heath_line_end_date', models.DateField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('Logo_name', models.CharField(blank=True, max_length=45)),
                ('Piece', models.OneToOneField(primary_key=True, to='gowan.Piece', serialize=False)),
                ('logo_description', models.CharField(blank=True, max_length=200)),
                ('stamp_name', models.CharField(blank=True, max_length=45)),
                ('picture', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='maker_link_piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MakerLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('maker_name', models.CharField(blank=True, max_length=45)),
                ('maker_location', models.CharField(blank=True, max_length=45)),
                ('maker_start_date', models.DateField(blank=True, null=True)),
                ('maker_stop_date', models.DateField(blank=True, null=True)),
                ('maker_description', models.CharField(blank=True, max_length=200)),
                ('maker_pieces', models.ManyToManyField(to='gowan.Piece', through='gowan.maker_link_piece')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='material_link_piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MaterialLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('material_name', models.CharField(blank=True, max_length=45)),
                ('material_description', models.CharField(blank=True, max_length=100)),
                ('material_pieces', models.ManyToManyField(to='gowan.Piece', through='gowan.material_link_piece')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='method_link_piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MethodLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('method_name', models.CharField(blank=True, max_length=45)),
                ('method_description', models.CharField(blank=True, max_length=500)),
                ('method_pieces', models.ManyToManyField(to='gowan.Piece', through='gowan.method_link_piece')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SetCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('set_collection_name', models.CharField(blank=True, max_length=45)),
                ('setcollection_location', models.CharField(blank=True, max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='setCollection_link_piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('Piece', models.ForeignKey(to='gowan.Piece')),
                ('SetCollection', models.ForeignKey(to='gowan.SetCollection')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='setcollection',
            name='set_collection_piece',
            field=models.ManyToManyField(to='gowan.Piece', through='gowan.setCollection_link_piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='method_link_piece',
            name='MethodLookup',
            field=models.ForeignKey(to='gowan.MethodLookup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='method_link_piece',
            name='Piece',
            field=models.ForeignKey(to='gowan.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='material_link_piece',
            name='MaterialLookup',
            field=models.ForeignKey(to='gowan.MaterialLookup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='material_link_piece',
            name='Piece',
            field=models.ForeignKey(to='gowan.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='maker_link_piece',
            name='MakerLookup',
            field=models.ForeignKey(to='gowan.MakerLookup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='maker_link_piece',
            name='Piece',
            field=models.ForeignKey(to='gowan.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='heathlinelookup',
            name='heath_line_pieces',
            field=models.ManyToManyField(to='gowan.Piece', through='gowan.heath_line_link_piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='heath_line_link_piece',
            name='heath_line',
            field=models.ForeignKey(to='gowan.HeathLineLookup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='heath_line_link_piece',
            name='piece',
            field=models.ForeignKey(to='gowan.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='glazelookup',
            name='glaze_pieces',
            field=models.ManyToManyField(to='gowan.Piece', through='gowan.glaze_link_piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='glaze_link_piece',
            name='glaze',
            field=models.ForeignKey(to='gowan.GlazeLookup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='glaze_link_piece',
            name='piece',
            field=models.ForeignKey(to='gowan.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documentation_link_piece',
            name='piece',
            field=models.ForeignKey(to='gowan.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documentation',
            name='documentation_pieces',
            field=models.ManyToManyField(to='gowan.Piece', through='gowan.documentation_link_piece'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='piece',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='piece',
            name='updated',
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='exhibition_description',
            field=models.CharField(blank=True, max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='exhibition_name',
            field=models.CharField(blank=True, max_length=45),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='piece',
            name='cataloguer',
            field=models.CharField(blank=True, max_length=45),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='piece',
            name='condition',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Condition',
        ),
        migrations.AlterField(
            model_name='publication',
            name='publication_author',
            field=models.CharField(blank=True, max_length=45),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='publication_media',
            field=models.CharField(blank=True, max_length=45),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='publication_name',
            field=models.CharField(blank=True, max_length=45),
            preserve_default=True,
        ),
    ]
