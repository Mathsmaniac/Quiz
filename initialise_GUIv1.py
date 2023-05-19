"""
initialise_guiv1.py
First component of quiz program.
In this I just set up the window and the maori words file
I made it print the Maori words for testing
"""


import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import ast


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        #Define styles
        s = ttk.Style()
        s.configure("TFrame", background="#bf3b3b")
        self.geometry("800x800")
        self.resizable(False, False)
        self.title("Te Reo Quiz")
        #Background image, using a label to display it
        self.bgimg = ImageTk.PhotoImage(Image.open("Dalle-Background.PNG"))
        self.bglabel = ttk.Label(self, i=self.bgimg)
        self.bglabel.pack()
        #Main frame of GUI
        self.mainframe = ttk.Frame(self.bglabel)
        self.mainframe.grid(row=0, column=0, padx=250, pady=250)
        #Label for testing
        ttk.Label(self.mainframe, text="test", background="#bf3b3b").grid(row=0, column=0, padx=150, pady=150)
        #Import words from file
        self.getdict()
        for word_type in self.words_dict:
            print(f"\n{word_type}: ")
            for term in self.words_dict[word_type]:
                print(f"{term}: {self.words_dict[word_type][term]}")


    #Function that imports maori words and definitions from file
    def getdict(self):
        with open("maori_words.txt", "r") as file:
            self.words_dict = ast.literal_eval(file.read())


if __name__ == "__main__":
    root = Root()
    tk.mainloop()
