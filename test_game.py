import pytest
from board import Board, Tile
from players import Player, Mediator, Game


class TestBoard:

    def setup_method(self, method):
        self.board = Board()
        self.med = Mediator(self.board)

    def test_put_cross_on_board(self):

        self.board[0][0] = 'X'

        assert self.board[0][0] == 'X'

class TestTile:

    def setup_method(self, method):
        self.board = Board()
        self.med = Mediator(self.board)

    def test_is_nought(self):
        tile = Tile('o')

        assert tile.is_nought()

    def test_is_cross(self):
        tile = Tile('x')

        assert tile.is_cross()

    def test_is_empty(self):
        tile = Tile('-')

        assert tile.is_empty()

    def test_invalid_tile(self):
        with pytest.raises(Exception):
            Tile('invalid')

    def test_board_initialise(self):
        for row in self.board:
            for tile in row:
                assert tile.is_empty()

class TestPlayer:

    def setup_method(self, method):
        self.board = Board()
        self.med = Mediator(self.board)

    def test_player_piece(self):
        player = Player('x')

        assert str(player.piece) == 'x'

    def test_player_makes_move(self):
        player = Player('x')
        self.board = Board()

        player.place_piece(self.board, (0,0))

        assert not self.board[0][0].is_empty()

class TestMediator:

    def setup_method(self, method):
        self.board = Board()
        self.med = Mediator(self.board)

    def test_place_on_empty_tile(self):
        tile = Tile('x')

        self.med.place_piece(tile, (0,0))

        assert self.med.board[0][0] == tile

    def test_place_non_empty_tile(self):
        tile = Tile('x')
        self.med.place_piece(tile, (0,0))

        with pytest.raises(Exception):
            self.med.place_piece(tile, (0, 0))

    def test_check_invalid_game(self):
        for col in range(3):
            self.board[0][col] = Tile('x')

        assert self.med.game_status() == 'invalid state'

    def test_check_new_game(self):
        assert self.med.game_status() == 'x turn'

    def test_check_noughts_turn(self):
        self.board[0][0] = Tile('x')

        assert self.med.game_status() == 'o turn'

    def test_check_cross_won(self):
        for col in range(3):
            self.board[0][col] = Tile('x')
        self.board[1][0] = Tile('o')
        self.board[1][1] = Tile('o')

        assert self.med.game_status() == 'x won'

    def test_check_nought_won(self):
        for col in range(3):
            self.board[0][col] = Tile('o')
        self.board[1][0] = Tile('x')
        self.board[1][1] = Tile('x')
        self.board[2][0] = Tile('x')

        assert self.med.game_status() == 'o won'

class TestGame:
    def setup_method(self, method):
        self.board = Board()
        self.med = Mediator(self.board)
        self.player1 = Player('x')
        self.player2 = Player('o')

    def test_start_game(self):
        Game(self.med, self.player1, self.player2)
