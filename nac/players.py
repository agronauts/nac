from board import Tile, TileNotEmptyError
from collections import Counter
from math import floor

import copy 
import itertools as it
import random
import abc

class Player:
    accepted_tokens = ['x', 'o', '-']

    def __init__(self, typ):
        self.piece = Tile(typ)
        self._med = None

    def place_piece(self, coord):
        assert self._med != None, 'Need to register with a Mediator'
        x, y = coord
        self._med.place_piece(self.piece, (x, y))
    
    @abc.abstractmethod
    def make_move(self):
        return


class AIPlayer(Player):

    def make_move(self):
        self.place_piece((random.randint(0,2), random.randint(0,2)))

class HumanPlayer(Player):
    def make_move(self):
        recv = int(input('Where do you want to put a piece [1-9]')) -1
        x, y = recv // 3, recv % 3
        self.place_piece((x, y))


class Mediator:

    def __init__(self, board, player1, player2):
        self.board = board
        self.p1 = player1
        self.p2 = player2
        self.p1._med = self
        self.p2._med = self

    def place_piece(self, piece, coord):
        x, y = coord
        if not self.board[x][y].is_empty():
            raise TileNotEmptyError()
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
        for line in it.chain(self.board.rows, self.board.cols, self.board.diags):
            if all(tile.is_cross() for tile in line):
                return 'x'
            elif all(tile.is_nought() for tile in line):
                return 'o'


    def __repr__(self):
        return 'Mediator(%s)' % repr(self.board)

