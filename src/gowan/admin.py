# soul
from django.contrib import admin
from gowan.models import Piece, Publication, Exhibition
from gowan.models import Condition


class PieceAdmin(admin.ModelAdmin):
	pass


admin.site.register(Piece, PieceAdmin)


class ConditionAdmin(admin.ModelAdmin):
	pass


admin.site.register(Condition, ConditionAdmin)



class PublicationAdmin(admin.ModelAdmin):
	pass


admin.site.register(Publication, PublicationAdmin)



class ExhibitionAdmin(admin.ModelAdmin):
	pass


admin.site.register(Exhibition, ExhibitionAdmin)
