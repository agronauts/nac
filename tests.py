import unittest
from board import Board

class BoardTest(unittest.TestCase):

    def test_put_cross_on_board(self):
        board = Board()

        board[0][0] = 'X'

        self.assertEqual(board[0][0], 'X')


def main():
    unittest.main()

if __name__ == '__main__':
    main()

