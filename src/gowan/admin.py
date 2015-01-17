
from django.contrib import admin
from gowan.models import Piece, ConditionChoice, Publication, Exhibition, Documentation, documentation_link_piece, GlazeLookup, glaze_link_piece, HeathLineLookup, heath_line_link_piece, Logo, MakerLookup, maker_link_piece, MaterialLookup, material_link_piece, MethodLookup, method_link_piece, SetCollection, setCollection_link_piece


@admin.register(Piece)
class PieceAdmin(admin.ModelAdmin):
    list_display = ('catalogue_id', 'heath_id', 'piece_name', 'piece_description', 'manufactured_date', 'length_inches', 'width_inches',
                    'height_inches', 'weight_ounces', 'length_mm', 'width_mm', 'height_mm', 'weight_grams', 'cataloguer', 'condition',)


# class PieceAdmin(admin.ModelAdmin):
# 	pass
# admin.site.register(Piece, PieceAdmin)


class ConditionChoiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(ConditionChoice, ConditionChoiceAdmin)


class PublicationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Publication, PublicationAdmin)


class ExhibitionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Exhibition, ExhibitionAdmin)


class DocumentationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Documentation, DocumentationAdmin)


class documentation_link_pieceAdmin(admin.ModelAdmin):
    pass
admin.site.register(documentation_link_piece, documentation_link_pieceAdmin)


class GlazeLookupAdmin(admin.ModelAdmin):
    pass
admin.site.register(GlazeLookup, GlazeLookupAdmin)


class glaze_link_pieceAdmin(admin.ModelAdmin):
    pass
admin.site.register(glaze_link_piece, glaze_link_pieceAdmin)


class HeathLineLookupAdmin(admin.ModelAdmin):
    pass
admin.site.register(HeathLineLookup, HeathLineLookupAdmin)


class heath_line_link_pieceAdmin(admin.ModelAdmin):
    pass
admin.site.register(heath_line_link_piece, heath_line_link_pieceAdmin)


class LogoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Logo, LogoAdmin)


class MakerLookupAdmin(admin.ModelAdmin):
    pass
admin.site.register(MakerLookup, MakerLookupAdmin)


class maker_link_pieceAdmin(admin.ModelAdmin):
    pass
admin.site.register(maker_link_piece, maker_link_pieceAdmin)


class MaterialLookupAdmin(admin.ModelAdmin):
    pass
admin.site.register(MaterialLookup, MaterialLookupAdmin)


class material_link_pieceAdmin(admin.ModelAdmin):
    pass
admin.site.register(material_link_piece, material_link_pieceAdmin)


class MethodLookupAdmin(admin.ModelAdmin):
    pass
admin.site.register(MethodLookup, MethodLookupAdmin)


class method_link_pieceAdmin(admin.ModelAdmin):
    pass
admin.site.register(method_link_piece, method_link_pieceAdmin)


class SetCollectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(SetCollection, SetCollectionAdmin)


class setCollection_link_pieceAdmin(admin.ModelAdmin):
    pass
admin.site.register(setCollection_link_piece, setCollection_link_pieceAdmin)
