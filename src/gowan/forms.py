from django import forms
from .models import Piece, GlazeLookup, Documentation, ConditionChoice, Exhibition, HeathLineLookup, Logo, MakerLookup, MaterialLookup, MethodLookup, Publication, SetCollection
from django.forms import ModelForm



class PieceForm(forms.ModelForm):
    class Meta:
        model = Piece
        fields = "__all__"

#Create the form class
class GlazeLookupForm(forms.ModelForm):
    class Meta:
    	model = GlazeLookup
    	fields = "__all__"

#form to add a glaze
#form = GlazeLookupForm(ModelForm)

#form to change an existing glaze
#glaze = GlazeLookup.objects.get(pk=1)
#form = GlazeLookupForm(instance=glaze)

#many to many
#Create the form class
class DocumentationForm(forms.ModelForm):
    class Meta:
      model = Documentation
      fields = "__all__"


class ExhibitionForm(forms.ModelForm):
    class Meta:
      model = Exhibition
      fields = "__all__"

class ConditionChoiceForm(forms.ModelForm):
    class Meta:
      model = ConditionChoice
      fields = "__all__"


class HeathLineLookupForm(forms.ModelForm):
  class Meta:
    model = HeathLineLookup
    fields = "__all__"


class LogoForm(forms.ModelForm):
  class Meta:
    model = Logo
    fields = "__all__"


class MakerLookupForm(forms.ModelForm):
  class Meta:
    model = MakerLookup
    fields = "__all__"


class MaterialLookupForm(forms.ModelForm):
  class Meta:
    model = MaterialLookup
    fields = "__all__"


class MethodLookupForm(forms.ModelForm):
  class Meta:
    model = MethodLookup
    fields = "__all__"


class PublicationForm(forms.ModelForm):
  class Meta:
    model = Publication
    fields = "__all__"


class SetCollectionForm(forms.ModelForm):
  class Meta:
    model = SetCollection
    fields = "__all__"





