from django.contrib import admin

# Register your models here.
from .models import Piece

class PieceAdmin(admin.ModelAdmin):
    class Meta:
        model = Piece
    
    admin.site.register(Piece, PieceAdmin)