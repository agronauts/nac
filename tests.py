import unittest
from board import Board, Tile 
from players import Player, Mediator

class BoardTest(unittest.TestCase):

    def test_put_cross_on_board(self):
        board = Board()

        board[0][0] = 'X'

        self.assertEqual(board[0][0], 'X')

class TileTest(unittest.TestCase):

    def test_is_nought(self):
        tile = Tile('o')

        self.assertTrue(tile.is_nought())

    def test_is_cross(self):
        tile = Tile('x')

        self.assertTrue(tile.is_cross())

    def test_is_empty(self):
        tile = Tile('-')

        self.assertTrue(tile.is_empty())

    def test_invalid_tile(self):
        with self.assertRaises(Exception) as context:
            Tile('invalid')
        self.assertEqual('Not a Tile type', str(context.exception))

class PlayerTest(unittest.TestCase):

    def test_player_piece(self):
        player = Player('x')

        self.assertEqual(player.piece, Tile('x'))

    def test_player_makes_move(self):
        player = Player('x')
        board = Board()

        player.place_piece(board, (0,0))

        self.assertFalse(board[0][0].is_empty())

class MediatorTest(unittest.TestCase):

    def setUp(self):
        board = Board()
        self.med = Mediator(board)

    def test_place_tile(self):
        tile = Tile('x')

        self.med.place_piece(tile, (0,0))

        self.assertTrue(self.med.board[0][0], tile)

    def test_place_non_empty_tile(self):
        tile = Tile('x')
        self.med.place_piece(tile, (0,0))

        with self.assertRaises(Exception) as context:
            self.med.place_piece(tile, (0, 0))

        self.assertEqual('Tile already occupied' , str(context.exception))


def main():
    unittest.main()

if __name__ == '__main__':
    main()

