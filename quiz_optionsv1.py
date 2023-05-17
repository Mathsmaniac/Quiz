import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        # Configure style
        s=ttk.Style()
        s.configure("TFrame", background="#bf3b3b")
        s.configure("TLabel", background="#bf3b3b")
        self.title("Te Reo Quiz")
        # Label for testing purposes
        ttk.Label(self, text="Main Window", font=("Arial", 30)).grid(row=0, column=0, padx=25, pady=25)
        # Create options toplevel
        options_level = Options(self)
        # Hide the window
        self.withdraw()


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
        self.option.set("colour")
        # Create radiobuttons
        self.r_colour = tk.Radiobutton(self.mainframe, image=self.colours_img, variable=self.option, value="colour")
        self.r_colour.grid(row=1, column=0, padx=20, pady=10)
        self.r_date = tk.Radiobutton(self.mainframe, image=self.dates_img, variable=self.option, value="date")
        self.r_date.grid(row=2, column=0, padx=20, pady=10)
        self.r_number = tk.Radiobutton(self.mainframe, image=self.numbers_img, variable=self.option, value="number")
        self.r_number.grid(row=3, column=0, padx=20, pady=10)

    def close_window(self):
        # Print selected item for testing
        print(self.option.get())
        root.deiconify()
        self.destroy()



if __name__ == "__main__":
    root = Root()
    tk.mainloop()
