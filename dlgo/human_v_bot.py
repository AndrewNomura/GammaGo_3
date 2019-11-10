from dlgo.agent import naive
from dlgo import goboard_slow as goboard
from dlgo import gotypes
from dlgo.utils import print_board, print_move, point_from_coords
from six.moves import input


def main():
    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bot = naive.RandomBot()

    while not game.is_over():
        print(chr(27) + "[2J")
        print_board(game.board)
        if game.next_player == gotypes.Player.black:
            human_move = input('-- ')
            point = point_from_coords(human_move.strip())
            move = goboard.Move.play(point)
        else:
            move = bot.select_move(game)
        print_move(game.next_player, move)
        game = game.apply_move(move)
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


if __name__ == '__main__':
    main()
