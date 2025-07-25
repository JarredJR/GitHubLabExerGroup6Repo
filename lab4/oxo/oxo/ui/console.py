from oxo.game import Game, InvalidMoveError

def run_console():
    game = Game()

    while True:
        print("\n" + str(game))
        if game.winner():
            print(f"Player {game.winner()} wins!")
            break
        if game.is_draw():
            print("It's a draw!")
            break

        try:
            pos = int(input(f"Player {game.current_player}, choose position (0-8): "))
            game.make_move(pos)
        except (ValueError, InvalidMoveError) as e:
            print("Invalid move:", e)

    print("\nFinal board:")
    print(game)
