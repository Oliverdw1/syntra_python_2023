
import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + entry.get())

# Create the main window
root = tk.Tk()
root.title("Tkinter Example")

# Create a label
label = tk.Label(root, text="Enter your name:")
label.pack()

# Create an entry widget
entry = tk.Entry(root)
entry.pack()

# Create a button
button = tk.Button(root, text="Say Hello", command=on_button_click)
button.pack()

# Start the Tkinter event loop
root.mainloop()