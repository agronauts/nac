class Tile(object):

    def __init__(self, typ):
        self._typ = typ.lower()
    
    def is_cross(self):
        return self._typ == 'x'

class Board:
    board = [['-' for _ in range(3)] for _ in range(3)]

    def __getitem__(self, index):
        return self.board[index]


