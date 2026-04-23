import streamlit as st,random
import tkinter as tk
import random

GRID_SIZE = 10

class FindDifferentGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Find the Different Number")
        self.buttons = []
        self.create_grid()
        self.new_round()

    def create_grid(self):
        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                btn = tk.Button(self.root, text="", width=6, height=2,
                                command=lambda r=i, c=j: self.check_click(r, c))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

    def new_round(self):
        # מספר אחיד
        self.common_number = random.randint(10, 99)

        # מספר שונה
        self.different_number = self.common_number
        while self.different_number == self.common_number:
            self.different_number = random.randint(10, 99)

        # מיקום רנדומלי
        self.diff_row = random.randint(0, GRID_SIZE - 1)
        self.diff_col = random.randint(0, GRID_SIZE - 1)

        # הצגה
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if i == self.diff_row and j == self.diff_col:
                    self.buttons[i][j].config(text=str(self.different_number))
                else:
                    self.buttons[i][j].config(text=str(self.common_number))

    def check_click(self, row, col):
        if row == self.diff_row and col == self.diff_col:
            self.new_round()
        else:
            print("נסה שוב!")

if __name__ == "__main__":
    root = tk.Tk()
    game = FindDifferentGame(root)
    root.mainloop()
