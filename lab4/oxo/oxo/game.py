from typing import List, Optional


class InvalidMoveError(Exception):
    """Custom error for invalid moves."""
    pass


class Game:
    """OOP Tic Tac Toe game logic."""
    EMPTY = " "
    PLAYERS = ("X", "O")
    WIN_LINES = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)              
    ]

    def __init__(self, first_player: str = "X"):
        if first_player not in self.PLAYERS:
            raise ValueError("first_player must be 'X' or 'O'")
        self.board: List[str] = [self.EMPTY] * 9
        self.current_player: str = first_player
        self._winner: Optional[str] = None
        self._move_count: int = 0

    def reset(self, first_player: str = "X") -> None:
        """Reset the game."""
        self.__init__(first_player)

    def make_move(self, pos: int) -> None:
        """Make a move for the current player."""
        if self._winner or self.is_draw():
            raise InvalidMoveError("Game already finished.")
        if not (0 <= pos <= 8):
            raise InvalidMoveError("Position must be between 0 and 8.")
        if self.board[pos] != self.EMPTY:
            raise InvalidMoveError("Cell already occupied.")

        self.board[pos] = self.current_player
        self._move_count += 1
        self._winner = self._compute_winner()

        if not self._winner:
            self._toggle_player()

    def legal_moves(self) -> List[int]:
        return [i for i, v in enumerate(self.board) if v == self.EMPTY]

    def winner(self) -> Optional[str]:
        return self._winner

    def is_draw(self) -> bool:
        return self._move_count == 9 and self._winner is None

    def board_as_rows(self) -> List[List[str]]:
        return [self.board[i:i + 3] for i in range(0, 9, 3)]

    def _toggle_player(self) -> None:
        self.current_player = "O" if self.current_player == "X" else "X"

    def _compute_winner(self) -> Optional[str]:
        for a, b, c in self.WIN_LINES:
            if self.board[a] != self.EMPTY and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def __str__(self) -> str:
        rows = self.board_as_rows()
        return "\n-----\n".join(" | ".join(r) for r in rows)
