"""
quiz_frameworkv3.py
In this version, I added some convenience updates
For example, the quiz starts with the text box ready to type in,
pressing a button will not take focus away from text box
delete everything inside the text box after 'next'
Also bound the "check" and "next" buttons to the "Enter" key
and added a label explaining this
Also added feedback label
"""

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        # Define styles
        s = ttk.Style()
        s.configure("GUIFrame.TFrame", background="#bf3b3b")
        s.configure("GUILabel.TLabel", background="#bf3b3b")
        s.configure("InfoLabel.TLabel", background="#bf3b3b",
                    font=("Arial", 8))
        s.configure("Macron.TButton", width=3)
        self.geometry("800x800")
        self.resizable(False, False)
        self.title("Te Reo Quiz")
        # Counter for question variable for testing
        self.question_count = 1
        # Variable for question
        self.question = tk.StringVar()
        self.question.set(f"Question {self.question_count}")
        # Variable for user's answer
        self.answer = tk.StringVar()
        # Background image, using a label to display it
        self.bgimg = ImageTk.PhotoImage(Image.open("Dalle-Background.PNG"))
        self.bglabel = ttk.Label(self, i=self.bgimg)
        self.bglabel.pack()
        # Main frame of GUI
        self.mainframe = ttk.Frame(self.bglabel, style="GUIFrame.TFrame")
        self.mainframe.grid(row=0, column=0, padx=250, pady=250)
        # Question label
        self.qlabel = ttk.Label(self.mainframe, text=self.question.get(),
                                font=("Arial", 20), style="GUILabel.TLabel")
        self.qlabel.grid(row=0, column=0, padx=10, pady=10)
        # Answer entry box
        self.answerbox = ttk.Entry(self.mainframe, textvariable=self.answer,
                                   width=22)
        self.answerbox.grid(row=2, column=0, padx=10, pady=10)
        self.answerbox.focus_set()
        # Buttons to insert special characters, in their own frame
        self.buttonframe = ttk.Frame(self.mainframe, style="GUIFrame.TFrame")
        self.buttonframe.grid(row=1, column=0, padx=50)
        self.buttonlabel = ttk.Label(self.buttonframe, style="GUILabel.TLabel",
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
        self.checkbutton.grid(row=5, column=0, padx=10, pady=(10, 0))
        # Bind return key to check function
        self.bind("<Return>", lambda event: self.check())
        # Information label for return keybinding
        self.infolabel = ttk.Label(self.mainframe, text="(Press 'enter')",
                                   style="InfoLabel.TLabel")
        self.infolabel.grid(row=6, column=0, pady=(0, 10), sticky="n")
        # Label for when question is checked. Starts off blank
        self.answerlabel = ttk.Label(self.mainframe, text="",
                                     font=("Arial", 15),
                                     style="GUILabel.TLabel")
        self.answerlabel.grid(row=3, column=0)
        # Label for feedback
        self.feedbacklabel = ttk.Label(self.mainframe, text="",
                                       font=("Arial", 11),
                                       style="GUILabel.TLabel")
        self.feedbacklabel.grid(row=4, column=0)

    def check(self):
        if self.answer.get() != "":
            print(self.answer.get())
            # Rebind return key to next function
            self.bind("<Return>", lambda event: self.next())
            # Just shows message "checked" for testing at the moment
            self.answerlabel.configure(text="checked")
            # Just says "feedback here" at the moment
            self.feedbacklabel.configure(text="feedback here")
            # Change checkbutton to say "next"
            self.checkbutton.configure(text="Next", command=self.next)
        else:
            # Show error message if it's blank
            tk.messagebox.showerror(title="Error",
                                    message="Please enter an answer")

    def insert(self, character):
        self.answerbox.insert(tk.INSERT, character)
        self.answerbox.focus_set()

    def next(self):
        # Rebind return key to check function
        self.bind("<Return>", lambda event: self.check())
        # Hide answer and feedback label and put checkbutton back to "check"
        self.answerlabel.configure(text="")
        self.checkbutton.configure(text="Check", command=self.check)
        self.feedbacklabel.configure(text="")
        # Update question label for testing
        self.question_count += 1
        self.question.set(f"Question {self.question_count}")
        self.qlabel.config(text=self.question.get())
        # Clear entry box
        self.answerbox.delete("0", "end")
        # Give entry box focus
        self.answerbox.focus_set()


if __name__ == "__main__":
    root = Root()
    tk.mainloop()
