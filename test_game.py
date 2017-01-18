import unittest
import pytest
from board import Board, Tile 
from players import Player, Mediator


class BoardTest(unittest.TestCase):

    def setup_method(self, method):
        self.board = Board()
        self.med = Mediator(self.board)

    def test_put_cross_on_board(self):

        self.board[0][0] = 'X'

        self.assertEqual(self.board[0][0], 'X')

class TileTest(unittest.TestCase):

    def setup_method(self, method):
        self.board = Board()
        self.med = Mediator(self.board)

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

    def test_board_initialise(self):
        pass

class PlayerTest(unittest.TestCase):

    def setup_method(self, method):
        self.board = Board()
        self.med = Mediator(self.board)

    def test_player_piece(self):
        player = Player('x')

        self.assertEqual(player.piece, Tile('x'))

    def test_player_makes_move(self):
        player = Player('x')
        self.board = Board()

        player.place_piece(self.board, (0,0))

        self.assertFalse(self.board[0][0].is_empty())

class MediatorTest(unittest.TestCase):

    def setup_method(self, method):
        self.board = Board()
        self.med = Mediator(self.board)

    def test_place_on_empty_tile(self):
        tile = Tile('x')

        self.med.place_piece(tile, (0,0))

        self.assertTrue(self.med.board[0][0], tile)

    def test_place_non_empty_tile(self):
        tile = Tile('x')
        print(self.med.board)
        self.med.place_piece(tile, (0,0))

        with pytest.raises(Exception):
            self.med.place_piece(tile, (0, 0))


def main():
    unittest.main()

if __name__ == '__main__':
    main()

