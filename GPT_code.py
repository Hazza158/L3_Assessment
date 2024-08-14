import tkinter as tk
import csv

# Function to load the CSV data
def load_csv_data(file_path):
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Function to display the next question
def next_question():
    global current_question, score
    if current_question < len(data):
        god_name.set(data[current_question]['God Name'])
        correct_answer.set(data[current_question]['Correct Answer'])
    else:
        question_label.config(text="Quiz Complete!")
        god_name.set("")
        button1.config(state=tk.DISABLED)
        button2.config(state=tk.DISABLED)

# Function to check the user's answer
def check_answer(user_answer):
    global current_question, score
    if user_answer == correct_answer.get():
        score += 1
        score_label.config(text=f"Score: {score}")
    current_question += 1
    next_question()

# Function to show help message
def show_help():
    help_message = "Click the correct button to identify whether the god is Greek or Roman."
    tk.messagebox.showinfo("Help", help_message)

# Initialize variables
current_question = 0
score = 0

# Load CSV data
data = load_csv_data('00_gods_data.csv')

# Set up the GUI
root = tk.Tk()
root.title("Greek or Roman Gods Quiz")

# Title Label
title_label = tk.Label(root, text="Greek or Roman Gods Quiz", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2)

# Question Label
question_label = tk.Label(root, text="Is this god Greek or Roman?", font=("Helvetica", 14))
question_label.grid(row=1, column=0, columnspan=2)

# God Name Label
god_name = tk.StringVar()
god_label = tk.Label(root, textvariable=god_name, font=("Helvetica", 14))
god_label.grid(row=2, column=0, columnspan=2)

# Buttons
correct_answer = tk.StringVar()
button1 = tk.Button(root, text="Greek", command=lambda: check_answer("Greek"))
button1.grid(row=3, column=0)
button2 = tk.Button(root, text="Roman", command=lambda: check_answer("Roman"))
button2.grid(row=3, column=1)

# Score Label
score_label = tk.Label(root, text=f"Score: {score}", font=("Helvetica", 14))
score_label.grid(row=4, column=0, columnspan=2)

# Help Button
help_button = tk.Button(root, text="Help", command=show_help)
help_button.grid(row=5, column=0, columnspan=2)

# Start the quiz
next_question()

# Run the GUI loop
root.mainloop()