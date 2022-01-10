from django.test import Client
from django.test import TestCase
from chess.piece.models import Piece
import json


class PieceIdTest(TestCase):
   
    def setUp(self):
        self.client = Client()   
        self.test_piece = Piece.objects.create(name='knight', color='black')
        self.response = self.client.get('/piece-id/', {'name': 'knight', 'color': 'black'}, HTTP_ACCEPT='application/json')

    def test_piece_id_url(self):     
        self.assertEqual(self.response.status_code, 200)

    def test_piece_id_url_query_params(self):
        self.assertEqual(self.response.request['QUERY_STRING'] , "name=knight&color=black")

    def test_piece_id_content(self):
        content = self.response.content.decode("utf-8")
        
        self.assertEqual(json.loads(content), {"id": self.test_piece.id})


class PieceMovesTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.test_piece = Piece.objects.create(name='knight', color='black')
        self.response = self.client.get('/piece-move/', {'id': '1', 'coordinate': 'b4'}, HTTP_ACCEPT='application/json')

    def test_piece_move_url(self):     
        self.assertEqual(self.response.status_code, 200)

    def test_piece_move_url_query_params(self):
        self.assertEqual(self.response.request['QUERY_STRING'] , "id=1&coordinate=b4")

    def test_piece_move_content_coordinate_a1_turn_one_and_turn_two(self):
        coordinate = 'a1'
        self.response = self.client.get('/piece-move/', {'id': '1', 'coordinate': coordinate}, HTTP_ACCEPT='application/json')
        content = self.response.content.decode("utf-8")
        content_json = json.loads(content)
        self.assertEqual(content_json["moves_turn_one"] , ['b3', 'c2'])
        self.assertEqual(content_json["moves_turn_two"] , 
            [['a1', 'a5', 'c1', 'c5', 'd2', 'd4'], 
            ['b4', 'a1', 'a3', 'd4', 'e1', 'e3']]
        )
    
    def test_piece_move_content_coordinate_d1_turn_one_and_turn_two(self):
        coordinate = 'd1'
        self.response = self.client.get('/piece-move/', {'id': '1', 'coordinate': coordinate}, HTTP_ACCEPT='application/json')
        content = self.response.content.decode("utf-8")
        content_json = json.loads(content)
        self.assertEqual(content_json["moves_turn_one"] , ['c3', 'b2', 'e3', 'f2'])
        self.assertEqual(content_json["moves_turn_two"] , 
            [['b1', 'b5', 'a2', 'a4', 'd1', 'd5', 'e2', 'e4'], 
            ['a4', 'c4', 'd1', 'd3'], 
            ['d1', 'd5', 'c2', 'c4', 'f1', 'f5', 'g2', 'g4'], 
            ['e4', 'd1', 'd3', 'g4', 'h1', 'h3']]
        )

    def test_piece_move_content_coordinate_h1_turn_one_and_turn_two(self):
        coordinate = 'h1'
        self.response = self.client.get('/piece-move/', {'id': '1', 'coordinate': coordinate}, HTTP_ACCEPT='application/json')
        content = self.response.content.decode("utf-8")
        content_json = json.loads(content)
        self.assertEqual(content_json["moves_turn_one"] , ['g3', 'f2'])
        self.assertEqual(content_json["moves_turn_two"] , 
            [['f1', 'f5', 'e2', 'e4', 'h1', 'h5'], 
            ['e4', 'd1', 'd3', 'g4', 'h1', 'h3']]
        )

    def test_piece_move_content_coordinate_h4_turn_one_and_turn_two(self):
        coordinate = 'h4'
        self.response = self.client.get('/piece-move/', {'id': '1', 'coordinate': coordinate}, HTTP_ACCEPT='application/json')
        content = self.response.content.decode("utf-8")
        content_json = json.loads(content)
        self.assertEqual(content_json["moves_turn_one"] , ['g2', 'g6', 'f3', 'f5'])
        self.assertEqual(content_json["moves_turn_two"] , 
            [['f4', 'e1', 'e3', 'h4'], 
            ['f4', 'f8', 'e5', 'e7', 'h4', 'h8'], 
            ['e1', 'e5', 'd2', 'd4', 'g1', 'g5', 'h2', 'h4'], 
            ['e3', 'e7', 'd4', 'd6', 'g3', 'g7', 'h4', 'h6']]
        )

    def test_piece_move_content_coordinate_h8_turn_one_and_turn_two(self):
        coordinate = 'h8'
        self.response = self.client.get('/piece-move/', {'id': '1', 'coordinate': coordinate}, HTTP_ACCEPT='application/json')
        content = self.response.content.decode("utf-8")
        content_json = json.loads(content)
        self.assertEqual(content_json["moves_turn_one"] , ['g6', 'f7'])
        self.assertEqual(content_json["moves_turn_two"] , 
            [['f4', 'f8', 'e5', 'e7', 'h4', 'h8'], 
            ['e5', 'd6', 'd8', 'g5', 'h6', 'h8']]
        )

    def test_piece_move_content_coordinate_e8_turn_one_and_turn_two(self):
        coordinate = 'e8'
        self.response = self.client.get('/piece-move/', {'id': '1', 'coordinate': coordinate}, HTTP_ACCEPT='application/json')
        content = self.response.content.decode("utf-8")
        content_json = json.loads(content)  
        self.assertEqual(content_json["moves_turn_one"] , ['d6', 'c7', 'f6', 'g7'])
        self.assertEqual(content_json["moves_turn_two"] , 
            [['c4', 'c8', 'b5', 'b7', 'e4', 'e8', 'f5', 'f7'], 
            ['b5', 'a6', 'a8', 'd5', 'e6', 'e8'], 
            ['e4', 'e8', 'd5', 'd7', 'g4', 'g8', 'h5', 'h7'], 
            ['f5', 'e6', 'e8', 'h5']]
        )

    def test_piece_move_content_coordinate_a8_turn_one_and_turn_two(self):
        coordinate = 'a8'
        self.response = self.client.get('/piece-move/', {'id': '1', 'coordinate': coordinate}, HTTP_ACCEPT='application/json')
        content = self.response.content.decode("utf-8")
        content_json = json.loads(content)
        self.assertEqual(content_json["moves_turn_one"] , ['b6', 'c7'])
        self.assertEqual(content_json["moves_turn_two"] , 
            [['a4', 'a8', 'c4', 'c8', 'd5', 'd7'], 
            ['b5', 'a6', 'a8', 'd5', 'e6', 'e8']]
        )

    def test_piece_move_content_coordinate_a5_turn_one_and_turn_two(self):
        coordinate = 'a5'
        self.response = self.client.get('/piece-move/', {'id': '1', 'coordinate': coordinate}, HTTP_ACCEPT='application/json')
        content = self.response.content.decode("utf-8")
        content_json = json.loads(content)
        self.assertEqual(content_json["moves_turn_one"] , ['b3', 'b7', 'c4', 'c6'])
        self.assertEqual(content_json["moves_turn_two"] , 
            [['a1', 'a5', 'c1', 'c5', 'd2', 'd4'], 
            ['a5', 'c5', 'd6', 'd8'], 
            ['b2', 'b6', 'a3', 'a5', 'd2', 'd6', 'e3', 'e5'], 
            ['b4', 'b8', 'a5', 'a7', 'd4', 'd8', 'e5', 'e7']]
        )

    def test_piece_move_content_coordinate_d4_turn_one_and_turn_two(self):
        coordinate = 'd4'
        self.response = self.client.get('/piece-move/', {'id': '1', 'coordinate': coordinate}, HTTP_ACCEPT='application/json')
        content = self.response.content.decode("utf-8")
        content_json = json.loads(content)
        self.assertEqual(content_json["moves_turn_one"] , ['c2', 'c6', 'b3', 'b5', 'e2', 'e6', 'f3', 'f5'])
        self.assertEqual(content_json["moves_turn_two"] , 
            [['b4', 'a1', 'a3', 'd4', 'e1', 'e3'], 
            ['b4', 'b8', 'a5', 'a7', 'd4', 'd8', 'e5', 'e7'], 
            ['a1', 'a5', 'c1', 'c5', 'd2', 'd4'], 
            ['a3', 'a7', 'c3', 'c7', 'd4', 'd6'], 
            ['d4', 'c1', 'c3', 'f4', 'g1', 'g3'], 
            ['d4', 'd8', 'c5', 'c7', 'f4', 'f8', 'g5', 'g7'], 
            ['e1', 'e5', 'd2', 'd4', 'g1', 'g5', 'h2', 'h4'], 
            ['e3', 'e7', 'd4', 'd6', 'g3', 'g7', 'h4', 'h6']
        ])

