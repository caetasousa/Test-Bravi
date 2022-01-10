from rest_framework import viewsets
from .models import Piece
from rest_framework.response import Response
from .serializers import PiecesSerializer
from django.shortcuts import get_object_or_404


class PieceId(viewsets.ViewSet):
    serializer_class = PiecesSerializer
    queryset = Piece.objects.all()

    def list(self, request):

        try:
            dado = request.query_params
            name, color = dado["name"], dado["color"]
            data = get_object_or_404(self.queryset, name=name, color=color)
        except:
            return Response('You need send the name of the part and the color in query parameters')
        
        return Response({"id": data.id})