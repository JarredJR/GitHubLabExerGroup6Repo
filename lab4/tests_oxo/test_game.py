import unittest
from oxo.oxo_logic import Game, InvalidMoveError

class TestGame(unittest.TestCase):

    def test_initial_state(self):
        game = Game()
        self.assertEqual(game.board, [" "] * 9)
        self.assertEqual(game.current_player, "X")
        self.assertIsNone(game.winner())
        self.assertFalse(game.is_draw())

    def test_valid_move(self):
        game = Game()
        game.make_move(0)
        self.assertEqual(game.board[0], "X")
        self.assertEqual(game.current_player, "O")

    def test_invalid_move_out_of_bounds(self):
        game = Game()
        with self.assertRaises(InvalidMoveError):
            game.make_move(10)

    def test_cell_already_taken(self):
        game = Game()
        game.make_move(0)
        with self.assertRaises(InvalidMoveError):
            game.make_move(0)

    def test_winner_detection(self):
        game = Game()
        moves = [0, 3, 1, 4, 2]  
        for m in moves:
            game.make_move(m)
        self.assertEqual(game.winner(), "X")

    def test_draw(self):
        game = Game()
        moves = [0,1,2,4,3,5,7,6,8]
        for m in moves:
            game.make_move(m)
        self.assertTrue(game.is_draw())
        self.assertIsNone(game.winner())

if __name__ == "__main__":
    unittest.main()
