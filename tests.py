import unittest
from board import Board, Tile

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
        self.assertTrue('Not a Tile type', str(context.exception))

def main():
    unittest.main()

if __name__ == '__main__':
    main()

