from board import Tile
from collections import Counter

import copy 
import itertools as it

class Player:
    accepted_tokens = ['x', 'o', '-']

    def __init__(self, typ):
        self.piece = Tile(typ)

    def place_piece(self, board, coord):
        x, y = coord
        board[x][y] = copy.copy(self.piece)

class Mediator:

    def __init__(self, board):
        self.board = board

    def place_piece(self, piece, coord):
        x, y = coord
        if not self.board[x][y].is_empty():
            raise Exception('Tile is not empty')
        self.board[x][y] = piece

    def game_status(self):
        ''' Return the status of the game '''
        counts = Counter([self.board[row][col]._typ for row in range(3) for col in range(3)])
        diff = counts['x'] - counts['o']
        if diff < 0 or 1 < diff:
            return 'invalid state'
        elif self._check_winner() == 'x':
            return 'x won'
        elif self._check_winner() == 'o':
            return 'o won'
        elif diff == 0:
            return 'x turn'
        elif diff == 1:
            return 'o turn'

    def _check_winner(self):
        # TODO Things
        for line in it.chain(self.board.rows, self.board.cols, self.board.diags):
            print('line', line)
            if all(tile.is_cross() for tile in line):
                return 'x'
            elif all(tile.is_nought() for tile in line):
                return 'o'


    def __repr__(self):
        return 'Mediator(%s)' % repr(self.board)

