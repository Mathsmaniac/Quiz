import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
# Imports dictionary of words and translations
from maori_words import maori_words_dict as words_dict


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        # Define styles
        s = ttk.Style()
        s.configure("TFrame", background="#bf3b3b")
        self.geometry("800x800")
        self.resizable(False, False)
        self.title("Te Reo Quiz")
        # Background image, using a label to display it
        self.bgimg = ImageTk.PhotoImage(Image.open("Dalle-Background.PNG"))
        self.bglabel = ttk.Label(self, i=self.bgimg)
        self.bglabel.pack()
        # Main frame of GUI
        self.mainframe = ttk.Frame(self.bglabel)
        self.mainframe.grid(row=0, column=0, padx=250, pady=250)
        # Label for testing
        ttk.Label(self.mainframe, text="test", background="#bf3b3b").grid(row=0, column=0, padx=150, pady=150)
        # Print words for testing
        for word_type in words_dict:
            print(f"\n{word_type}: ")
            for term in words_dict[word_type]:
                print(f"{term}: {words_dict[word_type][term]}")


if __name__ == "__main__":
    root = Root()
    tk.mainloop()
