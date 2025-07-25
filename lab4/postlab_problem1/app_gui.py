import tkinter as tk
from tkinter import messagebox
from postlab_problem1.oxo_logic import Game, InvalidMoveError

class TicTacToeGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe (OOP)")
        self.game = Game(first_player="X")
        self.buttons = []
        self.status_var = tk.StringVar(value=f"Player {self.game.current_player}'s turn")
        self._build_ui()

    def _build_ui(self):
        frame = tk.Frame(self)
        frame.pack(padx=10, pady=10)

        for i in range(9):
            btn = tk.Button(frame, text=" ", width=6, height=3,
                            command=lambda pos=i: self.handle_click(pos))
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

        status_label = tk.Label(self, textvariable=self.status_var, font=("Arial", 12))
        status_label.pack(pady=5)

        reset_btn = tk.Button(self, text="Reset", command=self.reset_game)
        reset_btn.pack()

    def handle_click(self, pos: int):
        try:
            self.game.make_move(pos)
            self.buttons[pos]["text"] = self.game.board[pos]
        except InvalidMoveError as e:
            messagebox.showerror("Invalid Move", str(e))
            return

        if self.game.winner():
            self.status_var.set(f"Player {self.game.winner()} wins!")
            messagebox.showinfo("Game Over", f"Player {self.game.winner()} wins!")
            self._disable_board()
        elif self.game.is_draw():
            self.status_var.set("It's a draw!")
            messagebox.showinfo("Game Over", "It's a draw!")
            self._disable_board()
        else:
            self.status_var.set(f"Player {self.game.current_player}'s turn")

    def _disable_board(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def reset_game(self):
        self.game.reset(first_player="X")
        for btn in self.buttons:
            btn.config(text=" ", state="normal")
        self.status_var.set(f"Player {self.game.current_player}'s turn")

if __name__ == "__main__":
    app = TicTacToeGUI()
    app.mainloop()
