import tkinter as tk

def insert_macron_a():
    text_input.insert(tk.INSERT, 'ā')

# Create the tkinter window
window = tk.Tk()

# Create the text input box
text_input = tk.Entry(window)

# Create the button that inserts 'ā' into the text input box
macron_button = tk.Button(window, text='Insert ā', command=insert_macron_a)

# Create a grid layout
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Add the text input box and button to the grid
text_input.grid(row=0, column=0, sticky="nsew")
macron_button.grid(row=1, column=0, sticky="nsew")
# Run the tkinter event loop
window.mainloop()

