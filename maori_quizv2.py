"""
maori_quizv2.py
Second version of assembled outcome
Integrated end-user testing:
Random word selection not selecting the same word twice
Showing missed words in end window
"""

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import random
# Imports dictionary of words and translations
from maori_words import maori_words_dict as words_dict


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
        # Set window options
        self.geometry("800x800")
        self.resizable(False, False)
        self.title("Te Reo Quiz")
        # Create options toplevel
        Options(self)
        # Hide the window
        self.withdraw()
        # Set question counter and counter for right and wrong questions
        self.question_count = 1
        self.right_count = 0
        # Make dictionary to store what the user got wrong
        # to display in results window
        self.wrong_dict = {"one": "tahi", "two": "rua"}
        # Background image, using a label to display it
        self.bgimg = ImageTk.PhotoImage(Image.open("Dalle-Background.PNG"))
        self.bglabel = ttk.Label(self, i=self.bgimg)
        self.bglabel.pack()
        # Set variable for quiz type
        self.quiz_type = ""
        # Variable for question
        self.question = tk.StringVar()
        # Variable for user's answer
        self.answer = tk.StringVar()
        # Main frame
        self.mainframe = ttk.Frame(self.bglabel, style="GUIFrame.TFrame")
        self.mainframe.grid(row=0, column=0, padx=250, pady=250)
        # Question label
        self.qlabel = ttk.Label(self.mainframe, text=self.question.get(),
                                font=("Arial", 20), style="GUILabel.TLabel",
                                justify="center")
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
            # Rebind return key to next function
            self.bind("<Return>", lambda event: self.next())
            # Check answer
            print(self.answer.get())
            checked = self.check_answer(self.answer.get())
            # Just shows message "checked" for testing at the moment
            self.answerlabel.configure(text=checked[0])
            # Just says "feedback here" at the moment
            self.feedbacklabel.configure(text=checked[1])
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
        self.question_count += 1
        self.ask_question()
        # If ten questions have been done, show results
        if self.question_count == 11:
            Results_toplevel(self)
            self.withdraw()
        # Clear entry box
        self.answerbox.delete("0", "end")
        # Give entry box focus
        self.answerbox.focus_set()

    def ask_question(self):
        # Convert dictionary keys of the type to a list
        keys_list = list(words_dict[self.quiz_type].keys())
        self.chosen = ""
        # Choose word and format question
        self.chosen = random.choice(keys_list)
        self.question.set(f"What is the Māori translation for \n{self.chosen}? ")
        self.qlabel.config(text=self.question.get())

    def check_answer(self, answer):
        # Get correct word
        correct = words_dict[self.quiz_type][self.chosen]
        # Check if write and output feedback
        if answer.lower() == correct.lower():
            self.right_count += 1
            return ["Correct", "Well done"]
        else:
            return ["Incorrect", f"The correct answer is {correct}"]

class Options(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Options Toplevel")
        # Create mainframe
        self.mainframe = ttk.Frame(self)
        self.mainframe.grid(row=0, column=0)
        # If the toplevel is closed, program closes
        self.protocol("WM_DELETE_WINDOW", quit)
        # Create continue button
        continue_button = ttk.Button(self.mainframe, text="Continue", command=self.close_window)
        continue_button.grid(row=4, column=0, padx=10, pady=10)
        # Create title
        title_label = ttk.Label(self.mainframe, text="Choose Quiz Type", font=("Arial", 30))
        title_label.grid(row=0, column=0, padx=10, pady=10)
        # Define images
        self.colours_img = ImageTk.PhotoImage(Image.open("colours_img.jpg").resize((150, 100)))
        self.dates_img = ImageTk.PhotoImage(Image.open("calendar_img.png").resize((150, 100)))
        self.numbers_img = ImageTk.PhotoImage(Image.open("numbers_img.jpg").resize((150, 100)))
        # Define variable for radiobuttons
        self.option = tk.StringVar()
        self.option.set("colours")
        # Create radiobuttons
        self.r_colour = tk.Radiobutton(self.mainframe, image=self.colours_img, variable=self.option, value="colours")
        self.r_colour.grid(row=1, column=0, padx=20, pady=10)
        self.r_date = tk.Radiobutton(self.mainframe, image=self.dates_img, variable=self.option, value="days_months")
        self.r_date.grid(row=2, column=0, padx=20, pady=10)
        self.r_number = tk.Radiobutton(self.mainframe, image=self.numbers_img, variable=self.option, value="numbers")
        self.r_number.grid(row=3, column=0, padx=20, pady=10)

    def close_window(self):
        # Print selected item for testing
        root.quiz_type = self.option.get()
        root.question.set(root.ask_question())
        root.deiconify()
        root.answerbox.focus_set()
        self.destroy()

class Results_toplevel(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Results!")
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
        self.quitbutton.grid(row=3, column=1, padx=20, pady=20)
        self.againbutton = ttk.Button(self.mainframe, text="Play Again",
                                      command=self.play_again)
        self.againbutton.grid(row=3, column=0, padx=20, pady=20)
        # Create label to show results
        self.r_label = ttk.Label(self.mainframe,
                                 text=f"You got {root.right_count}/10"
                                 " marks correct!",
                                 font=("Arial", 15), style="GUILabel.TLabel")
        self.r_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        # Info label for wrong words
        self.i_wrong_label = ttk.Label(self.mainframe, text="", font=("Arial", 12), style="GUILabel.TLabel")
        self.i_wrong_label.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
        if root.wrong_dict != {}:
            self.i_wrong_label.configure(text="Here are your mistakes:")
        # Label to display words the user got wrong
        self.wrong_text = ""
        for item in root.wrong_dict:
            self.wrong_text += f"'{item}' translates to '{root.wrong_dict[item]}'\n"
        self.wrong_label = ttk.Label(self.mainframe, text=self.wrong_text,
                                     style="GUILabel.TLabel")
        self.wrong_label.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

    def play_again(self):
        root.question_count = 1
        root.right_count = 0
        root.wrong_dict = {}
        Options(root)
        self.destroy()


if __name__ == "__main__":
    root=Root()
    tk.mainloop()
