from board import Tile

class Player:
    accepted_tokens = ['x', 'o', '-']

    def __init__(self, typ):
        self.piece = Tile(typ)

