
from __future__ import unicode_literals
from django.db import models


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

	def __str__(self):
		return self.piece_name


conditions = (
	('a', 'Pristine' ),
	('b', 'Used, good'),
	('c', 'Used, worn'),
	('d', 'Cracked / chipped'),
	('e', 'Broken'),
	)
#choice
class ConditionChoice(models.Model):

	name = models.CharField(max_length=60)
	condition = models.CharField(max_length=1, choices=conditions)

	def __str__(self):
		return self.name

#many to many
class Documentation(models.Model):
	documentation_name = models.CharField(max_length=45, blank=True)
	documentation_pieces = models.ManyToManyField(Piece, through="documentation_link_piece")

	def __str__(self):
		return self.documentation_name

class documentation_link_piece(models.Model):
	documentation = models.ForeignKey(Documentation)
	piece = models.ForeignKey(Piece)
	documentation_date = models.DateField(blank=True, null=True)
	documentation_author = models.CharField(max_length=45, blank=True)
	documentation_media = models.CharField(max_length=45, blank=True)
	documentation_location = models.CharField(max_length=45, blank=True)

	def __str__(self):
		return "documentation_link_piece"

#one to many
#one exhibition has many pieces, foreign key is exibition_id and is in pieces
#exhibition = models.ForeignKey('exhibition')
class Exhibition(models.Model):
	exhibition_name = models.CharField(max_length=45, blank=True)
	exhibition_date = models.DateField(blank=True, null=True)
	exhibition_description = models.CharField(max_length=1000, blank=True)

	def __str__(self):
		return self.exhibition_name

#many to many

class GlazeLookup(models.Model):
	glaze_name = models.CharField(max_length=45, blank=True)
	glaze_pieces = models.ManyToManyField(Piece, through="glaze_link_piece")
	glaze_description = models.CharField(max_length=500, blank=True)
	glaze_begin_date = models.DateField(blank=True, null=True)
	glaze_end_date = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.glaze_name

class glaze_link_piece(models.Model):
	piece = models.ForeignKey(Piece)
	glaze = models.ForeignKey(GlazeLookup)

	def __str__(self):
		return "glaze_link_piece"

#many to many
class HeathLineLookup(models.Model):
	heath_line_name = models.CharField(max_length=45, blank=True)
	heath_line_pieces = models.ManyToManyField(Piece, through="heath_line_link_piece")
	heath_line_begin_date = models.DateField(blank=True, null=True)
	heath_line_end_date = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.heath_line_name

class heath_line_link_piece(models.Model):
	piece = models.ForeignKey(Piece)
	heath_line = models.ForeignKey(HeathLineLookup)

	def __str__(self):
		return "heath_line_link_piece"

#one to one
class Logo(models.Model):
	Logo_name = models.CharField(max_length=45, blank=True)
	Piece = models.OneToOneField(Piece, primary_key=True)
	#Logo = models.OneToOneField(Logo, related_name='Logo')
	logo_description = models.CharField(max_length=200, blank=True)
	stamp_name = models.CharField(max_length=45, blank=True)
	picture = models.TextField(blank=True)

	def __str__(self):
		return self.Logo_name


#many to many
class MakerLookup(models.Model):
	maker_name = models.CharField(max_length=45, blank=True)
	maker_pieces = models.ManyToManyField(Piece, through="maker_link_piece")
	maker_location = models.CharField(max_length=45, blank=True)
	maker_start_date = models.DateField(blank=True, null=True)
	maker_stop_date = models.DateField(blank=True, null=True)
	maker_description = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.maker_name

class maker_link_piece(models.Model):
	Piece = models.ForeignKey(Piece)
	MakerLookup = models.ForeignKey(MakerLookup)

	def __str__(self):
		return "maker_link_piece"

#many to many
class MaterialLookup(models.Model):
	material_name = models.CharField(max_length=45, blank=True)
	material_pieces = models.ManyToManyField(Piece, through="material_link_piece")
	material_description = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.material_name

class material_link_piece(models.Model):
	Piece = models.ForeignKey(Piece)
	MaterialLookup = models.ForeignKey(MaterialLookup)

	def __str__(self):
		return "material_link_piece"

#many to many
class MethodLookup(models.Model):
	method_name = models.CharField(max_length=45, blank=True)
	method_pieces = models.ManyToManyField(Piece, through="method_link_piece")
	method_description = models.CharField(max_length=500, blank=True)

	def __str__(self):
		return self.method_name

class method_link_piece(models.Model):
	Piece = models.ForeignKey(Piece)
	MethodLookup = models.ForeignKey( MethodLookup)

	def __str__(self):
		return "method_link_piece"




#one to many
#one publication has many pieces, foreign key is publication_id and is in table 'Pieces'
#publication = models.ForeignKey('publication')

class Publication(models.Model):
	publication_name = models.CharField(max_length=45, blank=True)
	publication_date = models.DateField(blank=True, null=True)
	publication_author = models.CharField(max_length=45, blank=True)
	publication_media = models.CharField(max_length=45, blank=True)

	def __str__(self):
		return self.publication_name



#many to many
class SetCollection(models.Model):
	set_collection_name = models.CharField(max_length=45, blank=True)
	set_collection_piece = models.ManyToManyField(Piece, through="setCollection_link_piece")
	setcollection_location = models.CharField(max_length=45, blank=True)

	def __str__(self):
		return self.set_collection_name

class setCollection_link_piece(models.Model):
	Piece = models.ForeignKey(Piece)
	SetCollection = models.ForeignKey(SetCollection)
	date = models.DateField(blank=True, null=True)
	description = models.CharField(max_length=1000, blank=True)

	def __str__(self):
		return "setCollection_link_piece"
