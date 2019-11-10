from dlgo import agent
from dlgo.agent import naive
from dlgo import goboard
from dlgo import gotypes
from dlgo.utils import print_board, print_move
from dlgo import scoring
import time


def main():
    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: agent.naive.RandomBot(),
        gotypes.Player.white: agent.naive.RandomBot(),
    }
    while not game.is_over():
        time.sleep(0)  # <1>

        print(chr(27) + "[2J")  # <2>
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)
    black_score = scoring.evaluate_territory(game.board).num_black_stones
    black_score = black_score + scoring.evaluate_territory(game.board).num_black_territory
    white_score = scoring.evaluate_territory(game.board).num_white_stones
    white_score = white_score + scoring.evaluate_territory(game.board).num_white_territory
    if black_score > white_score:
        print("\nPlayer Black Wins: ")
        print(black_score)
    elif white_score > black_score:
        print("\nPlayer White Wins: ")
        print(white_score)
    else:
        print("Draw")


if __name__ == '__main__':
    main()
