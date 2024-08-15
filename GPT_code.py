from tkinter import *
from functools import partial  # To prevent unwanted windows
import csv
import random  # allows the questions to be randomized

# holds all the GUI formatting, question randomising and correct answer check
class QuizPlay:
    def __init__(self):
        self.quiz_box = Toplevel()

        # If users press cross at top, closes help and
        # 'releases' help button
        self.quiz_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_quiz))

        # Create buttons
        self.create_buttons()

    def create_buttons(self):
        # Button 1
        btn1 = Button(self.quiz_box, text="Start Quiz", command=self.start_quiz)
        btn1.grid(row=0, column=0, padx=10, pady=10)

        # Button 2
        btn2 = Button(self.quiz_box, text="Show Score", command=self.show_score)
        btn2.grid(row=0, column=1, padx=10, pady=10)

        # Button 3
        btn3 = Button(self.quiz_box, text="Help", command=self.show_help)
        btn3.grid(row=1, column=0, padx=10, pady=10)

        # Button 4
        btn4 = Button(self.quiz_box, text="Exit", command=self.close_quiz)
        btn4.grid(row=1, column=1, padx=10, pady=10)

    def start_quiz(self):
        # Placeholder for starting the quiz
        print("Quiz started")

    def show_score(self):
        # Placeholder for showing score
        print("Score: [Your Score Here]")

    def show_help(self):
        # Placeholder for showing help information
        print("Help: [Help Information Here]")

    def get_all_gods(self):
        file = open("00_gods_Data.csv", "r")
        var_all_gods = list(csv.reader(file, delimiter=","))
        file.close()

        # removes first entry in list (ie: the header row).
        var_all_gods.pop(0)
        return var_all_gods

    # *** DONT USE IN MAIN BASE (KILLS THE ROOT) ***
    def close_quiz(self):
        self.quiz_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Greek Gods Quiz")

    # Create an instance of QuizPlay to show the quiz window
    quiz = QuizPlay()

    root.mainloop()
