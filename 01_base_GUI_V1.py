from tkinter import *
from functools import partial  # To prevent unwanted windows
from datetime import date
import re


class Converter:

    def __init__(self):

        # Initialise variables (such as the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        self.all_calculations = []

        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # Set up GUI Frame
        self.quiz_frame = Frame(padx=10, pady=10)
        self.quiz_frame.grid()

        self.quiz_heading = Label(self.quiz_frame,
                                  text="Greek Gods Quiz",
                                  font=("Arial", "16", "bold")
                                  )
        self.quiz_heading.grid(row=0)

        instructions = "In this quiz you will input the amount of " \
                        "questions you want to answer, then press the " \
                        "'START' button to begin the quiz." \

        self.quiz_instructions = Label(self.quiz_frame,
                                       text=instructions,
                                       wrap=250, width=40,
                                       justify="left")
        self.quiz_instructions.grid(row=1)

        self.quiz_entry = Entry(self.quiz_frame,
                                font=("Arial", "14")
                                )
        self.quiz_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.output_label = Label(self.quiz_frame, text="",
                                  fg="#9C0000")
        self.output_label.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)