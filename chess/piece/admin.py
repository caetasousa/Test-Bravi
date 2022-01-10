from django.contrib import admin
from . import models


@admin.register(models.Piece)
class ChessAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')

