import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def button_click(answer):
    messagebox.showinfo("Answer Selected", f"You selected Answer {answer}")

# Create the main window
root = tk.Tk()
root.title("Quiz")

# Create four answer buttons
button1 = tk.Button(root, text="Answer 1", command=lambda: button_click(1))
button1.pack(pady=5)

button2 = tk.Button(root, text="Answer 2", command=lambda: button_click(2))
button2.pack(pady=5)

button3 = tk.Button(root, text="Answer 3", command=lambda: button_click(3))
button3.pack(pady=5)

button4 = tk.Button(root, text="Answer 4", command=lambda: button_click(4))
button4.pack(pady=5)

# Start the tkinter main loop
root.mainloop()
