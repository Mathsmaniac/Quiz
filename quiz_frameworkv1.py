"""
quiz_frameworkv1.py
Third component of quiz project
Built on top of initialise_GUIv2, but not including maori word import
This component sets up the GUI window for when I actually add the questions
and answers and working.
In this version I just added the widgets, including the buttons to insert
special characters.
"""

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        # Define styles
        s = ttk.Style()
        s.configure("TFrame", background="#bf3b3b")
        s.configure("TLabel", background="#bf3b3b")
        s.configure("Macron.TButton", width=3)
        self.geometry("800x800")
        self.resizable(False, False)
        self.title("Te Reo Quiz")
        # Variable for question
        self.question = tk.StringVar()
        self.question.set("Question 1")
        # Variable for user's answer
        self.answer = tk.StringVar()
        # Background image, using a label to display it
        self.bgimg = ImageTk.PhotoImage(Image.open("Dalle-Background.PNG"))
        self.bglabel = ttk.Label(self, i=self.bgimg)
        self.bglabel.pack()
        # Main frame of GUI
        self.mainframe = ttk.Frame(self.bglabel)
        self.mainframe.grid(row=0, column=0, padx=250, pady=250)
        # Question label
        self.qlabel = ttk.Label(self.mainframe, text=self.question.get(),
                                font=("Arial", 20))
        self.qlabel.grid(row=0, column=0, padx=10, pady=10)
        # Answer entry box
        self.answerbox = ttk.Entry(self.mainframe, textvariable=self.answer,
                                   width=22)
        self.answerbox.grid(row=2, column=0, padx=10, pady=10)
        # Buttons to insert special characters, in their own frame
        self.buttonframe = ttk.Frame(self.mainframe)
        self.buttonframe.grid(row=1, column=0, padx=50)
        self.buttonlabel = ttk.Label(self.buttonframe,
                                     text="Press to Insert Characters")
        self.buttonlabel.grid(row=0, column=0, columnspan=5)
        self.abutton = ttk.Button(self.buttonframe, text="ā",
                                  command=lambda: self.insert("ā"),
                                  style="Macron.TButton")
        self.abutton.grid(row=1, column=0)
        self.ebutton = ttk.Button(self.buttonframe, text="ē",
                                  command=lambda: self.insert("ē"),
                                  style="Macron.TButton")
        self.ebutton.grid(row=1, column=1)
        self.ibutton = ttk.Button(self.buttonframe, text="ī",
                                  command=lambda: self.insert("ī"),
                                  style="Macron.TButton")
        self.ibutton.grid(row=1, column=2)
        self.obutton = ttk.Button(self.buttonframe, text="ō",
                                  command=lambda: self.insert("ō"),
                                  style="Macron.TButton")
        self.obutton.grid(row=1, column=3)
        self.ubutton = ttk.Button(self.buttonframe, text="ū",
                                  command=lambda: self.insert("ū"),
                                  style="Macron.TButton")
        self.ubutton.grid(row=1, column=4)
        # "Check" button
        self.checkbutton = ttk.Button(self.mainframe, text="Check",
                                      command=self.check)
        self.checkbutton.grid(row=3, column=0, padx=10, pady=10)

    def check(self):
        print(self.answer.get())

    def insert(self, character):
        self.answerbox.insert(tk.INSERT, character)


if __name__ == "__main__":
    root = Root()
    tk.mainloop()
