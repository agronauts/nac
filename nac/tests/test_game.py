
import pytest
import contextlib

from ..board import Board, Tile, TileNotEmptyError
from ..players import Player, Mediator




class TestBoard:

    def setup_method(self, method):
        self.board = Board()
        p1 = Player('x')
        p2 = Player('o')
        self.med = Mediator(self.board, p1, p2)

    def test_put_cross_on_board(self):

        self.board[0][0] = 'X'

        assert self.board[0][0] == 'X'

class TestTile:

    def setup_method(self, method):
        self.board = Board()
        p1 = Player('x')
        p2 = Player('o')
        self.med = Mediator(self.board, p1, p2)

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
        with pytest.raises(TileNotEmptyError):
            Tile('invalid')

    def test_board_initialise(self):
        for row in self.board:
            for tile in row:
                assert tile.is_empty()

class TestPlayer:

    def setup_method(self, method):
        self.board = Board()
        p1 = Player('x')
        p2 = Player('o')
        self.med = Mediator(self.board, p1, p2)

    def test_player_piece(self):
        player = Player('x')

        assert str(player.piece) == 'x'

def test_player_makes_move(monkeypatch):
    class MockMediator:
        def __init__(self):
            pass
        def place_piece(*_):
            pass
    player = Player('x')
    monkeypatch.setattr(player, '_med', MockMediator())

    player.place_piece((0,0))


class TestMediator:

    def setup_method(self, method):
        self.board = Board()
        p1 = Player('x')
        p2 = Player('o')
        self.med = Mediator(self.board, p1, p2)

    def test_place_on_empty_tile(self):
        tile = Tile('x')

        self.med.place_piece(tile, (0,0))

        assert self.med.board[0][0] == tile

    def test_place_non_empty_tile(self):
        tile = Tile('x')
        self.med.place_piece(tile, (0,0))

        with pytest.raises(TileNotEmptyError):
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

class TestInterface:
    def setup_method(self, method):
        self.board = Board()
        self.p1 = Player('x')
        self.p2 = Player('o')
        self.med = Mediator(self.board, self.p1, self.p2)

    def test_play_valid_game(self):
        assert self.med.game_status() == 'x turn'
        self.p1.place_piece((0,0))
        assert self.med.game_status() == 'o turn'
        self.p2.place_piece((1,0))
        assert self.med.game_status() == 'x turn'
        self.p1.place_piece((0,1))
        assert self.med.game_status() == 'o turn'
        self.p2.place_piece((1,2))
        assert self.med.game_status() == 'x turn'
        self.p1.place_piece((0,2))
        assert self.med.game_status() == 'x won'

    def test_play_valid_game_with_one_invalid_move(self):
        with valid_game(self.med, self.p1, self.p2):
            with pytest.raises(TileNotEmptyError):
                self.p2.place_piece((0,0))

    def test_play_valid_game_with_many_invalid_moves(self):
        with valid_game(self.med, self.p1, self.p2):
            with pytest.raises(TileNotEmptyError):
                self.p2.place_piece((0,0))
                assert self.med.game_status() == 'o turn'
                self.p2.place_piece((0,0))
                assert self.med.game_status() == 'o turn'
                self.p2.place_piece((0,0))

@contextlib.contextmanager
def valid_game(med, p1, p2):
    assert med.game_status() == 'x turn'
    p1.place_piece((0,0))
    yield
    assert med.game_status() == 'o turn'
    p2.place_piece((1,0))
    assert med.game_status() == 'x turn'
    p1.place_piece((0,1))
    assert med.game_status() == 'o turn'
    p2.place_piece((1,2))
    assert med.game_status() == 'x turn'
    p1.place_piece((0,2))
    assert med.game_status() == 'x won'
