from board import Board, Tile, TileNotEmptyError
from players import HumanPlayer, AIPlayer, Mediator
from time import sleep

def start_game(board, med, p1, p2):
    count = 0
    while 'won' not in med.game_status() and count < 100:
        count += 1
        print(board)
        print('\n')
        try:
            if med.game_status() == 'x turn':
                p1.make_move()
            elif med.game_status() == 'o turn':
                p2.make_move()
        except TileNotEmptyError:
            pass
        sleep(.4)

def main():
    print('Starting game')
    board = Board()
    p1 = HumanPlayer('x')
    p2 = AIPlayer('o')
    med = Mediator(board, p1, p2)
    start_game(board, med, p1, p2)
    print(board)
    print(med.game_status())

if __name__ == '__main__':
    main()
