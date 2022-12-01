import tkinter as tk


class Menu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.font = ("Times New Roman", 20)

        lbl_main = tk.Label(self, text="Меню", font=self.font)

        lbl_main.grid(row=0, columnspan=2, column=1)
