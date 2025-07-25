from postlab_problem1.oxo_logic import Game, InvalidMoveError

def print_board(game: Game):
    print()
    for i, row in enumerate(game.board_as_rows()):
        print(" {} | {} | {} ".format(*row))
        if i < 2:
            print("---+---+---")
    print()

def main():
    game = Game(first_player="X")

    while True:
        print_board(game)
        if game.winner():
            print(f"Player {game.winner()} wins!")
            break
        if game.is_draw():
            print("It's a draw!")
            break

        try:
            pos = int(input(f"Player {game.current_player}, enter position (0-8): "))
            game.make_move(pos)
        except (ValueError, InvalidMoveError) as e:
            print("Invalid move:", e)

    print("Final board:")
    print_board(game)

if __name__ == "__main__":
    main()
