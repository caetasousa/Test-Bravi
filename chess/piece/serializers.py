from rest_framework import serializers
from .models import Piece


class PiecesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piece
        fields = ('name', 'color')