from board import Tile

import copy 

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
        self.board[x][y] = piece

