import tkinter as tk
from tkinter import messagebox

# Tic Tac Toe game using Tkinter
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title('Tic Tac Toe')
        self.current_player = 'X'  # Player 'X' starts the game
        self.buttons = []  # To store button references
        self.board = [' ' for _ in range(9)]  # Empty board
        
        self.create_widgets()

    # Function to create the Tic Tac Toe board buttons
    def create_widgets(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text=' ', font=('Arial', 40), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)


    # Function to handle button clicks
    def on_click(self, row, col):
        idx = row * 3 + col
        if self.board[idx] == ' ':
            self.board[idx] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_win():
                messagebox.showinfo('Game Over', f'Player {self.current_player} wins!')
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo('Game Over', 'The game is a draw!')
                self.reset_game()
            else:
                # Switch player
                self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            messagebox.showwarning('Invalid Move', 'This spot is already taken!')

    # Function to check if a player has won
    def check_win(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                          (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] == self.current_player:
                return True
        return False

    # Function to check if the board is full (draw)
    def check_draw(self):
        return all(spot != ' ' for spot in self.board)

    # Function to reset the game
    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        for row in self.buttons:
            for button in row:
                button.config(text=' ')

# Main application window
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
