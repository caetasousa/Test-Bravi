from django.test import TestCase
from chess.piece.models import Piece


class TestCreatePiece(TestCase):
    
    def setUp(self):
        self.test_piece = Piece.objects.create(name='knight', color='black')
        self.piece = Piece.objects.get(id=1)

    def test_create(self):
        self.assertTrue(Piece.objects.exists())

    def test_piece_name_field(self):
        name = self.piece.name
        self.assertEqual(name, 'knight')

    def test_piece_color_field(self):
        color = self.piece.color
        self.assertEqual(color, 'black')