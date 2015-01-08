
from __future__ import unicode_literals
from django.db import models
#models fixedup one
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.

class Piece(models.Model):

	catalogue_id = models.CharField(max_length=45)
	heath_id = models.CharField(max_length=45, blank=True)
	piece_name = models.CharField(max_length=45, blank=True)
	piece_description = models.CharField(max_length=2000, blank=True)
	manufactured_date = models.DateField(blank=True, null=True)
	length_inches = models.IntegerField(blank=True, null=True)
	width_inches = models.IntegerField(blank=True, null=True)
	height_inches = models.IntegerField(blank=True, null=True)
	weight_ounces = models.IntegerField(blank=True, null=True)
	length_mm = models.IntegerField(blank=True, null=True)
	width_mm = models.IntegerField(blank=True, null=True)
	height_mm = models.IntegerField(blank=True, null=True)
	weight_grams = models.IntegerField(blank=True, null=True)
	cataloguer = models.CharField(max_length=45, blank=True)
	catalogue_date = models.DateField(blank=True, null=True)
	condition = models.IntegerField(blank=True, null=True)
	#many to one
	exhibition = models.ForeignKey('Exhibition')
	publication = models.ForeignKey('Publication')

#choice
class ConditionChoice(models.Model):
	conditions = (
		('a', 'Pristine' ),
		('b', 'Used, good'),
		('c', 'Used, worn'),
		('d', 'Cracked / chipped'),
		('e', 'Broken'),
		)
	name = models.CharField(max_length=60)
	condition = models.CharField(max_length=1, choices=conditions)

#many to many
class Documentation(models.Model):
	documentation_name = models.CharField(max_length=45, blank=True)
	documentation_pieces = models.ManyToManyField(Piece, through="documentation_link_piece", through_fields=('Documentation', 'Piece'))

class documentation_link_piece(models.Model):
	documentation = models.ForeignKey(Documentation)
	piece = models.ForeignKey(Piece)
	documentation_date = models.DateField(blank=True, null=True)
	documentation_author = models.CharField(max_length=45, blank=True)
	documentation_media = models.CharField(max_length=45, blank=True)
	documentation_location = models.CharField(max_length=45, blank=True)

#one to many
#one exhibition has many pieces, foreign key is exibition_id and is in pieces
#exhibition = models.ForeignKey('exhibition')
class Exhibition(models.Model):
	exhibition_name = models.CharField(max_length=45, blank=True)
	exhibition_date = models.DateField(blank=True, null=True)
	exhibition_description = models.CharField(max_length=1000, blank=True)

#many to many

class GlazeLookup(models.Model):
	glaze_name = models.CharField(max_length=45, blank=True)
	glaze_pieces = models.ManyToManyField(Piece, through="glaze_link_piece", through_fields=('GlazeLookup', 'Piece'))
	glaze_description = models.CharField(max_length=500, blank=True)
	glaze_begin_date = models.DateField(blank=True, null=True)
	glaze_end_date = models.DateField(blank=True, null=True)

class glaze_link_piece(models.Model):
	piece = models.ForeignKey(Piece)
	glaze = models.ForeignKey(GlazeLookup)

#many to many
class HeathLineLookup(models.Model):
	heath_line_name = models.CharField(max_length=45, blank=True)
	heath_line_pieces = models.ManyToManyField(Piece, through=" heath_line_link_piece", through_fields=('HeathLineLookup', 'Piece'))
	heath_line_begin_date = models.DateField(blank=True, null=True)
	heath_line_end_date = models.DateField(blank=True, null=True)

class heath_line_link_piece(models.Model):
	piece = models.ForeignKey(Piece)
	heath_line = models.ForeignKey(HeathLineLookup)

#one to one
class Logo(models.Model):
	Logo_name = models.CharField(max_length=45, blank=True)
	Piece = models.OneToOneField(Piece, primary_key=True)
	#Logo = models.OneToOneField(Logo, related_name='Logo')

	logo_description = models.CharField(max_length=200, blank=True)
	stamp_name = models.CharField(max_length=45, blank=True)
	picture = models.TextField(blank=True)


#many to many
class MakerLookup(models.Model):
	maker_name = models.CharField(max_length=45, blank=True)
	maker_pieces = models.ManyToManyField(Piece, through="maker_link_piece", through_fields=('MakerLookup', 'Piece'))
	maker_location = models.CharField(max_length=45, blank=True)
	maker_start_date = models.DateField(blank=True, null=True)
	maker_stop_date = models.DateField(blank=True, null=True)
	maker_description = models.CharField(max_length=200, blank=True)

class maker_link_piece(models.Model):
	Piece = models.ForeignKey(Piece)
	MakerLookup = models.ForeignKey(MakerLookup)

#many to many
class MaterialLookup(models.Model):
	material_name = models.CharField(max_length=45, blank=True)
	material_pieces = models.ManyToManyField(Piece, through="Material_link_piece", through_fields=('MaterialLookup', 'Piece'))
	material_description = models.CharField(max_length=100, blank=True)

class Material_link_piece(models.Model):
	Piece = models.ForeignKey(Piece)
	MaterialLookup = models.ForeignKey(MaterialLookup)

#many to many
class MethodLookup(models.Model):
	method_name = models.CharField(max_length=45, blank=True)
	method_pieces = models.ManyToManyField(Piece, through="Method_link_piece", through_fields=(' MethodLookup', 'Piece'))
	method_description = models.CharField(max_length=500, blank=True)

class Method_link_piece(models.Model):
	Piece = models.ForeignKey(Piece)
	MethodLookup = models.ForeignKey( MethodLookup)




#one to many
#one publication has many pieces, foreign key is publication_id and is in table 'Pieces'
#publication = models.ForeignKey('publication')

class Publication(models.Model):
	publication_name = models.CharField(max_length=45, blank=True)
	publication_date = models.DateField(blank=True, null=True)
	publication_author = models.CharField(max_length=45, blank=True)
	publication_media = models.CharField(max_length=45, blank=True)



#many to many
class SetCollection(models.Model):
	set_collection_name = models.CharField(max_length=45, blank=True)
	set_collection_piece = models.ManyToManyField(Piece, through="SetCollection_link_piece", through_fields=('SetCollection', 'Piece'))
	setcollection_location = models.CharField(max_length=45, blank=True)

class SetCollection_link_piece(models.Model):
	Piece = models.ForeignKey(Piece)
	SetCollection = models.ForeignKey(SetCollection)
	date = models.DateField(blank=True, null=True)
	description = models.CharField(max_length=1000, blank=True)

# Create your models here.