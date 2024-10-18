from tkinter import *
from functools import partial  # To prevent unwanted windows
import csv
import random  # allows the questions to be randomized


# holds all the GUI formatting, question randomising and correct answer check
class QuizPLay:
    def __init__(self, how_many):

        self.quiz_box = Toplevel()

        # If users press cross at top, closes help and
        # 'releases' help button
        self.quiz_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_quiz))

        # get all the gods to use in the quiz
        self.all_gods = self.get_all_gods()

        self.quiz_frame = Frame(self.quiz_box, padx=10, pady=10)
        self.quiz_frame.grid()

        rounds_heading = "Choose - Round 1 of {}".format(how_many)
        self.choose_heading = Label(self.quiz_frame, text=rounds_heading,
                                    font=("Arial", "16", "bold")
                                    )
        self.choose_heading.grid(row=0)

        instructions = "Choose the answer that you think is correct from the selection below." \
                       "After you choose your answer, the quiz will display if the answer you chose" \
                       "was correct or incorrect."
        self.instructions_label = Label(self.quiz_frame, text=instructions,
                                        wraplength=350, justify="left")
        self.instructions_label.grid(row=1)

    # gets the Gods data from CSV file
    def get_all_gods(self):
        file = open("00_gods_Data.csv", "r")
        var_all_gods = list(csv.reader(file, delimiter=","))
        file.close()

        # removes first entry in list (ie: the header row).
        var_all_gods.pop(0)
        return var_all_gods

    # *** DONT USE IN MAIN BASE (KILLS THE ROOT) ***
    def close_quiz(self):
        self.quiz_box.destroy()  # close only the quiz window


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Greek Gods Quiz")
    root.mainloop()
