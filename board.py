class Tile:
    accepted_tokens = ['x', 'o', '-']

    def __init__(self, typ):
        token = typ.lower()
        if token not in self.accepted_tokens:
            raise Exception('Not a Tile type')
        self._typ = typ.lower()

    def is_cross(self):
        return self._typ == 'x'

    def is_nought(self):
        return self._typ == 'o'

    def is_empty(self):
        return self._typ == '-'

class Board:
    _board = [[Tile('-') for _ in range(3)] for _ in range(3)]

    def __setitem__(self, index, item):
        tile = Tile(item)
        self._board[index] = tile

    def __getitem__(self, index):
        return self._board[index]


