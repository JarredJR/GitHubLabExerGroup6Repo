import unittest
from postlab_problem1.oxo_logic import Game, InvalidMoveError

class TestGame(unittest.TestCase):

    def test_initial_state(self):
        g = Game()
        self.assertEqual(g.board, [" "] * 9)
        self.assertEqual(g.current_player, "X")
        self.assertIsNone(g.winner())
        self.assertFalse(g.is_draw())

    def test_make_valid_move(self):
        g = Game()
        g.make_move(0)
        self.assertEqual(g.board[0], "X")
        self.assertEqual(g.current_player, "O")

    def test_illegal_move_out_of_bounds(self):
        g = Game()
        with self.assertRaises(InvalidMoveError):
            g.make_move(9)

    def test_illegal_move_cell_occupied(self):
        g = Game()
        g.make_move(0)
        with self.assertRaises(InvalidMoveError):
            g.make_move(0)

    def test_win_detection_row(self):
        g = Game()
        g.make_move(0)  # X
        g.make_move(3)  # O
        g.make_move(1)  # X
        g.make_move(4)  # O
        g.make_move(2)  # X -> wins
        self.assertEqual(g.winner(), "X")

    def test_draw_detection(self):
        g = Game()
        moves = [0,1,2,4,3,5,7,6,8]  # draw
        for m in moves:
            g.make_move(m)
        self.assertTrue(g.is_draw())
        self.assertIsNone(g.winner())

    def test_cant_move_after_game_over(self):
        g = Game()
        g.make_move(0)  # X
        g.make_move(3)  # O
        g.make_move(1)  # X
        g.make_move(4)  # O
        g.make_move(2)  # X wins
        with self.assertRaises(InvalidMoveError):
            g.make_move(5)

if __name__ == "__main__":
    unittest.main()
