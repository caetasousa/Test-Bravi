from rest_framework import viewsets
from .models import Piece
from rest_framework.response import Response
from .serializers import PiecesSerializer
from django.shortcuts import get_object_or_404
from .chess_moves import move_knight_turn_one, move_knight_turn_two


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


class PieceMove(viewsets.ViewSet):
    serializer_class = PiecesSerializer
    queryset = Piece.objects.all()

    def list(self, request):
        
        try:
            dado = request.query_params
            id, coordinate = dado["id"], dado["coordinate"]
            data = get_object_or_404(self.queryset, id=id)
            response = move_knight_turn_one(coordinate)

            turn_two = move_knight_turn_two(response)
            
        except:
            return Response('You need send the id and coordinate in query parameters')

        return Response({'piece': data.name, 'color': data.color, 'moves_turn_one': response, 'moves_turn_two': turn_two})