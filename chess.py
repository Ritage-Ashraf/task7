import tkinter as tk

class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        self.board = ChessBoard()
        self.buttons = [[None for _ in range(8)] for _ in range(8)]
        self.create_widgets()

    def create_widgets(self):
        for row in range(8):
            for col in range(8):
                button = tk.Button(self.root, text=self.board.board[row][col], width=4, height=2,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_button_click(self, row, col):
        # Handle piece selection and movement
        # This function needs to be implemented
        pass

    def update_board(self):
        for row in range(8):
            for col in range(8):
                piece = self.board.board[row][col]
                self.buttons[row][col].config(text=str(piece) if piece != ' ' else '')
