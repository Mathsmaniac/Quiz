"""
results_windowv2.py
Trialling of results_window component
In this one I use a message_box popup instead of a seperate toplevel
This introduces a lot of simplicity into the component
But it comes with the cost of decreased aesthetics
"""

import tkinter as tk
from tkinter import ttk, messagebox


# Main window to create toplevel and define styles
# Stays up to demonstrate grab_set
class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        # Define styles
        s = ttk.Style()
        s.configure("GUIFrame.TFrame", background="#bf3b3b")
        s.configure("GUILabel.TLabel", background="#bf3b3b")
        self.title("Main window")
        # Label for testing purposes
        ttk.Label(self, text="Main Window",
                  font=("Arial", 30)).grid(row=0, column=0,
                                           padx=25, pady=25)
        retry = tk.messagebox.askretrycancel("Results!", f"You got {mark}/10,"
                                             " would you like to retry"
                                             " the quiz?")
        if retry == True:
            self.play_again()
        else:
            quit()

    def play_again(self):
        print("Play Again")


if __name__ == "__main__":
    mark = input("Marks: ")
    root = Root()
    tk.mainloop()
