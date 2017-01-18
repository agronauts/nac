class Board:
    board = [['-' for _ in range(3)] for _ in range(3)]

    def put_cross(self, x, y):
        self.board[x][y]

    def __getitem__(self, index):
        return self.board[index]
