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
	cataloguer = models.CharField(max_length=45, blank=True, default="")
	catalogue_date = models.DateField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	condition = models.ForeignKey('Condition')
	exhibition = models.ForeignKey('Exhibition')
	publication = models.ForeignKey('Publication')

	def __str__(self):
		return self.piece_name


class Condition(models.Model):
	PRISTINE = 1
	GOOD = 2
	WORN = 3
	CRACKED = 4
	BROKEN = 5
	CONDITION_CHOICES = (
		(PRISTINE, 'Pristine' ),
		(GOOD, 'Used, good'),
		(WORN, 'Used, worn'),
		(CRACKED, 'Cracked / chipped'),
		(BROKEN, 'Broken'),
	)
	condition = models.IntegerField(null=True, blank=True),
	choices = CONDITION_CHOICES,
	default = GOOD


def __str__(self):
	return self.condition


class Publication(models.Model):
	publication_name = models.CharField(max_length=45, blank=True, default="")
	publication_date = models.DateField(blank=True, null=True)
	publication_author = models.CharField(max_length=45, blank=True, default="")
	publication_media = models.CharField(max_length=45, blank=True, default="")

	def __str__(self):
		return self.publication_name


class Exhibition(models.Model):
	exhibition_name = models.CharField(max_length=45, blank=True, default="")
	exhibition_date = models.DateField(blank=True, null=True)
	exhibition_description = models.CharField(max_length=1000, blank=True,
											  default="")

	def __str__(self):
		return self.exhibition_name
