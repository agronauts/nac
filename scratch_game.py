from board import Board
from players import AIPlayer, Mediator
def game():
    p1 = AIPlayer('x')
    p2 = AIPlayer('o')
    board = Board()
    med = Mediator(board, p1, p2)
    while 'won' not in med.game_status():
        for player in [p1, p2]:
            player.make_move()
            yield med.game_status()
g = game()
for i in range(5):
    print(next(g)
