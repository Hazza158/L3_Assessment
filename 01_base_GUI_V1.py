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
        self.button_frame = Frame(self.quiz_frame)
        self.button_frame.grid(row=4)

        self.quiz_start_button = Button(self.button_frame,
                                        text="Start Quiz",
                                        bg="06D6A0",
                                        fg=button_fg,
                                        font=button_font,
                                        width=10)
        self.quiz_start_button.grid(row=0, column=1, padx=5, pady=5)



class DisplayHelp:

    def __init__(self, partner):
        # setup dialogue box and background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # disable help button
        partner.to_help_button.config(state=DISABLED)

        # If users press cross at top, closes help and
        # 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300,
                                height=200,
                                bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        bg=background,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To use the program, simply enter the temperature " \
                    "you wish to convert and then choose to convert " \
                    "to either degrees Celsius (centigrade) or " \
                    "Fahrenheit..  \n\n" \
                    " Note that -273 degrees C " \
                    "(-459 F) is absolute zero (the coldest possible " \
                    "temperature).  If you try to convert a " \
                    "temperature that is less than -273 degrees C, " \
                    "you will get an error message. \n\n " \
                    "To see your " \
                    "calculation history and export it to a text " \
                    "file, please click the 'History / Export' button."
        self.help_text_label = Label(self.help_frame, bg=background,
                                     text=help_text, wrap=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help,
                                                     partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    # closes help dialogue (used by button and x at top of dialogue)
    def close_help(self, partner):
        # Put help button back to normal...
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()