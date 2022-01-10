from django.test import TestCase
from chess.piece.models import Piece
from chess.piece.serializers import PiecesSerializer


class PostSerializerTestCase(TestCase):
    
    def setUp(self):
        self.test_piece = Piece.objects.create(name='knight', color='black')
        self.serializer = PiecesSerializer(instance=self.test_piece)
        self.data = self.serializer.data

    def test_fields_piece_serializer(self):
        self.assertEqual(set(self.data.keys()), set(['name', 'color']))

    def test_content_serializer_name(self):
        self.assertEqual(self.data['name'], self.test_piece.name)

    def test_content_serializer_color(self):
        self.assertEqual(self.data['color'], self.test_piece.color)
