from tkinter import *
from functools import partial  # To prevent unwanted windows
import csv
import random  # allows the questions to be randomized


# holds all the GUI formatting, question randomising and correct answer check
class QuizPLay:
    def __init__(self):

        self.quiz_box = Toplevel()

        # If users press cross at top, closes help and
        # 'releases' help button
        self.quiz_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_quiz))

    def get_all_gods(self):
        file = open("00_gods_Data.csv", "r")
        var_all_gods = list(csv.reader(file, delimiter=","))
        file.close()

        # removes first entry in list (ie: the header row).
        var_all_gods.pop(0)
        return var_all_gods

    # *** DONT USE IN MAIN BASE (KILLS THE ROOT) ***
    def close_quiz(self):
        root.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Greek Gods Quiz")
    root.mainloop()
