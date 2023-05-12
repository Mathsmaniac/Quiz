import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


root = tk.Tk()
img1 = ImageTk.PhotoImage(Image.open("multi-color-rainbow-background.JPG"))
ttk.Button(root, text="Click", image=img1).grid(row=0, column=0)

tk.mainloop()
