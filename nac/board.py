class Tile:
    accepted_tokens = ['x', 'o', '-']

    def __init__(self, token):
        if token not in self.accepted_tokens:
            raise TileNotEmptyError('Not a Tile type')
        self._typ = token

    def is_cross(self):
        return self._typ == 'x'

    def is_nought(self):
        return self._typ == 'o'

    def is_empty(self):
        return self._typ == '-'

    def __eq__(self, other):
        if isinstance(other, str):
            return self._typ == other
        return self._typ == other._typ

    def __str__(self):
        return self._typ

    def __repr__(self):
        return "Tile(%s)" % repr(self._typ)


class Board:

    def __init__(self):
        self._board = [[Tile('-') for _ in range(3)] for _ in range(3)]
        self.rows = [row for row in self._board]
        self.cols = [[row[col] for col in range(3)] for row in self.rows]
        self.diags =[[self._board[row][col] for row, col in zip(range(3), range(3))],\
                     [self._board[row][col] for row, col in zip(range(3), range(2, -1, -1))]]

    def __setitem__(self, index, item):
        tile = Tile(item)
        self._board[index] = tile

    def __getitem__(self, index):
        return self._board[index]

    def __str__(self):
        rows = []
        for row in range(3):
            rows.append('|'.join(str(self._board[col][row]) for col in range(3)))
        return '\n-+-+-\n'.join(rows)

    def __repr__(self):
        return 'Board()'


class Error(Exception):
    pass

class TileNotEmptyError(Error):
    pass



