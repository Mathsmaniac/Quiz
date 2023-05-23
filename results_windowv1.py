"""
results_windowv1.py
Fifth and final component of quiz project before user testing
A simple toplevel that displays the amount of points received out of ten
Also has a 'quit' and a 'play again' button
Uses styles from quiz_frameworkv3.py for when it is integrated
"""

import tkinter as tk
from tkinter import ttk


# Main window to create toplevel and define styles
# Stays up to demonstrate grab_set
class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        # Define styles
        s = ttk.Style()
        s.configure("GUIFrame.TFrame", background="#bf3b3b")
        s.configure("GUILabel.TLabel", background="#bf3b3b")
        Results_toplevel(self)
        self.title("Main window")
        # Label for testing purposes
        ttk.Label(self, text="Main Window",
                  font=("Arial", 30)).grid(row=0, column=0,
                                           padx=25, pady=25)


class Results_toplevel(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Results!")
        self.marks = mark
        # If the toplevel is closed, program closes
        self.protocol("WM_DELETE_WINDOW", quit)
        # Grab_set window
        self.grab_set()
        self.focus_set()
        # Create mainframe
        self.mainframe = ttk.Frame(self, style="GUIFrame.TFrame")
        self.mainframe.grid(row=0, column=0)
        # Create buttons to quit or play again
        self.quitbutton = ttk.Button(self.mainframe, text="Quit", command=quit)
        self.quitbutton.grid(row=1, column=1, padx=20, pady=20)
        self.againbutton = ttk.Button(self.mainframe, text="Play Again",
                                      command=self.play_again)
        self.againbutton.grid(row=1, column=0, padx=20, pady=20)
        # Create label to show results
        self.r_label = ttk.Label(self.mainframe,
                                 text=f"You got {self.marks}/10"
                                 " marks correct!",
                                 font=("Arial", 15), style="GUILabel.TLabel")
        self.r_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    def play_again(self):
        print("Play Again")
        self.destroy()


if __name__ == "__main__":
    mark = input("Marks: ")
    root = Root()
    tk.mainloop()
