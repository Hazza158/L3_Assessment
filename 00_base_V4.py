from tkinter import *
from functools import partial  # To prevent unwanted windows
import csv
import random


# Choose rounds class - beginning of programme
class ChooseRounds:
    def __init__(self):
        self.custom_window = None
        button_fg = "#FFFFFF"
        button_font = ("Arial", "13", "bold")

        # Initialise variables (such as the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        # Set up GUI Frame
        self.intro_frame = Frame(padx=10, pady=10)
        self.intro_frame.grid()

        # Heading and introduction
        self.intro_heading_label = Label(self.intro_frame, text="Greek and Roman Gods",
                                         font=("Arial", "16", "bold"))
        self.intro_heading_label.grid(row=0)

        introduction = "This is a quiz about Greek and Roman gods!, " \
                       "to start click on either 5 or 10 rounds. " \
                       "Additionally, you can select the 'custom' " \
                       "rounds option. This will allow you to input " \
                       "however many rounds you wish to answer " \
                       "between 1-100. " \
                       "Enjoy!"
        self.choose_instructions_label = Label(self.intro_frame,
                                               text=introduction,
                                               wraplength=300, justify="left")
        self.choose_instructions_label.grid(row=1)

        # Setting up the "how many" frame
        self.how_many_frame = Frame(self.intro_frame)
        self.how_many_frame.grid(row=2)

        self.output_label = Label(self.intro_frame, text="",
                                  fg="#9C0000")
        self.output_label.grid(row=3)

        btn_colour_value = [
            ["#dce3de", 5],
            ["#dce3de", 10]
        ]

        for item in range(0, 2):
            self.rounds_button = Button(self.how_many_frame,
                                        fg=button_fg,
                                        bg=btn_colour_value[item][0],
                                        text="{}".format(btn_colour_value[item][1]),
                                        font=button_font, width=10,
                                        command=lambda i=item: self.to_quiz(btn_colour_value[i][1])
                                        )
            self.rounds_button.grid(row=0, column=item,
                                    padx=5, pady=5)

        self.custom_button = Button(self.how_many_frame,
                                    bg="#dce3de",
                                    fg=button_fg, text="Custom",
                                    font=button_font, width=10,
                                    command=lambda: self.custom_rounds()
                                    )
        self.custom_button.grid(row=0, column=2,
                                padx=5, pady=5)

    # Custom rounds - When "Custom" is clicked, should open a second window
    def custom_rounds(self):
        self.custom_window = Toplevel()
        self.custom_window.title("Custom Rounds")

        self.label = Label(self.custom_window, text="Enter a number between 1-100:")
        self.label.grid(row=0, padx=10, pady=10)

        self.entry = Entry(self.custom_window)
        self.entry.grid(row=1, padx=10, pady=10)
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.add_placeholder)

        # Output label for error messages
        self.output_label = Label(self.custom_window, text="",
                                  fg="#9C0000")
        self.output_label.grid(row=2, padx=10, pady=10)

        self.submit_button = Button(self.custom_window,
                                    text="Submit", bg="#009900",
                                    command=self.submit_custom_rounds)
        self.submit_button.grid(row=3, padx=10, pady=10)

        self.placeholder = "Enter a number"
        self.placeholder_color = "grey"
        self.default_color = self.entry.cget("fg")
        self.add_placeholder(None)

    # clear the placeholder box automatically when an incorrect response is submitted
    def clear_placeholder(self, event):
        if self.entry.get() == self.placeholder:
            self.entry.delete(0, END)
            self.entry.config(fg=self.default_color, bg="white")

    def add_placeholder(self, event):
        if not self.entry.get():
            self.entry.insert(0, self.placeholder)
            self.entry.config(fg=self.placeholder_color)

    # method to check the input for custom rounds
    # if invalid, provide error message
    def submit_custom_rounds(self):
        has_error = "no"

        try:
            num_rounds = int(self.entry.get())
            if 1 <= num_rounds <= 100:
                self.to_quiz(num_rounds)
                self.custom_window.destroy()
                self.custom_button.config(state=NORMAL)
            else:
                has_error = "yes"
                self.var_feedback.set("Oh No! \n"
                                      "You have input a number \n"
                                      "that isn't between 1-100 rounds! \n"
                                      "Please try again")
                self.output_label.config(fg="#9C0000")
                self.entry.config(bg="#F8CE00")
        except ValueError:
            has_error = "yes"
            self.var_feedback.set("Oh No! \n"
                                  "That doesnt look right! \n"
                                  "Please try again using\n"
                                  "a whole number between 1-100.")
            self.output_label.config(fg="#9C0000")
            self.entry.config(bg="#F8CE00")

        if has_error == "yes":
            self.var_has_error.set("yes")
            self.output_label.config(text=self.var_feedback.get())
        else:
            self.var_has_error.set("no")

    # To quiz function - start quiz when used
    def to_quiz(self, num_rounds):
        Quiz(num_rounds)

        # Hide root window (ie: hide rounds option window).
        root.withdraw()


# Grab data from the CSV file
def get_all_data():
    with open("00_gods_Data.csv", "r") as file:
        var_all_data = list(csv.reader(file, delimiter=","))
    # Remove the header row from the data.
    var_all_data.pop(0)
    return var_all_data


# The Play class handles the main gameplay.
class Quiz:
    def __init__(self, how_many):
        background = "#FFFFFF"
        # Initialize the user's score.
        self.user_score = 0
        # Create a new window for the quiz.
        self.quiz_box = Toplevel()

        # If users press cross at top, closes help
        self.quiz_box.protocol('WM_DELETE_WINDOW', partial(self.close_quiz))

        # Variables used to work out statistics, when game ends etc
        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)

        # Initialize rounds played and rounds won; set to 0
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        self.rounds_won = IntVar()
        self.rounds_won.set(0)

        # Load all data from the CSV file
        self.all_data = get_all_data()

        # Create the quiz frame.
        self.quiz_frame = Frame(self.quiz_box, width=300,
                                height=200, padx=10, pady=10,
                                bg=background)
        self.quiz_frame.grid()

        # Heading for the rounds.
        rounds_heading = f"Choose - Round 1 of {how_many}"
        self.choose_heading = Label(self.quiz_frame, text=rounds_heading,
                                    font=("Raleway", "16", "bold"),
                                    bg=background)
        self.choose_heading.grid(row=0)

        # Instructions for the quiz.
        instructions = "Analise the question below and then answer with " \
                       "what you think is the correct answer. " \
                       "If you are looking for more info or get " \
                       "stuck then select 'Help'. Good Luck."
        self.instructions_label = Label(self.quiz_frame, text=instructions,
                                        wraplength=350, justify="left",
                                        bg=background)
        self.instructions_label.grid(row=1, padx=5, pady=5)

        # Label for the current question.
        self.question_label = Label(self.quiz_frame, text="Is this God Greek or Roman?",
                                    wraplength=350, justify="center",
                                    font=("Helvetica", 16, "bold"), padx=5, pady=5,
                                    bg=background)
        self.question_label.grid(row=2)

        # Label for displaying the god's name.
        self.god_label = Label(self.quiz_frame, text="god name goes here",
                               bg="#8f8f8f", width=19, fg="#FFFFFF", font=("Raleway", "12", "bold"))
        self.god_label.grid(row=3, padx=5, pady=5)

        # Create the option buttons in a new frame.
        self.option_frame = Frame(self.quiz_frame)
        self.option_frame.grid(row=4)

        # Greek answer button.
        self.greek_button = Button(self.option_frame, fg="#FFFFFF", width=18, bg="#dce3de",
                                   text="Greek", font=("Arial", "12", "bold"),
                                   command=lambda: self.check_answer("Greek"))
        self.greek_button.grid(row=0, column=0, padx=5, pady=5)

        # Roman answer button.
        self.roman_button = Button(self.option_frame, fg="#FFFFFF", width=18, bg="#dce3de",
                                   text="Roman", font=("Arial", "12", "bold"),
                                   command=lambda: self.check_answer("Roman"))
        self.roman_button.grid(row=1, column=0, padx=5, pady=5)

        # displays usrs choice and result
        self.user_choice_label = Label(self.quiz_frame,
                                       text="Your answer will show up here!",
                                       bg="#8f8f8f", width=23, fg="#FFFFFF",
                                       justify="left")
        self.user_choice_label.grid(row=5, padx=5, pady=5)

        # Frame for round results and navigation.
        self.rounds_frame = Frame(self.quiz_frame)
        self.rounds_frame.grid(row=6, padx=5, pady=5)

        # current rounds result label
        self.round_results_label = Label(self.rounds_frame, text="Your score and round info will appear here",
                                         width=44,
                                         font=("Arial", 10),
                                         bg=background)
        self.round_results_label.grid(row=0, column=0)

        # Control frame for nav buttons.
        self.control_frame = Frame(self.quiz_frame)
        self.control_frame.grid(row=7)

        # self.start_over_button = Button(self.control_frame, text="START OVER",
                                        # fg="#FFFFFF", bg="#3bb4ff",
                                        # font=("Arial", 11, "bold"),
                                        # width=12,
                                        # padx=3, pady=3, justify= "center",
                                        # command=self.close_quiz
        # self.start_over_button.grid(row=0, column=1)

        # help button
        self.help_button = Button(self.control_frame, text="HELP",
                                  fg="#FFFFFF", bg="#dce3de",
                                  font=("Arial", 11, "bold"),
                                  width=12,
                                  padx=3, pady=3,
                                  command=self.get_help)
        self.help_button.grid(row=0, column=0)

        # next round button
        self.next_button = Button(self.control_frame, text="NEXT",
                                  fg="#FFFFFF", bg="#dce3de",
                                  font=("Arial", 11, "bold"),
                                  width=12, state=DISABLED,
                                  padx=3, pady=3,
                                  command=self.new_round)
        self.next_button.grid(row=0, column=2)

        # Start the first round.
        self.new_round()

    # Method to load data from the CSV file.

    # new round start
    def new_round(self):
        # Disable the next button at the start of each round.
        self.next_button.config(state=DISABLED)
        self.greek_button.config(state=NORMAL)
        self.roman_button.config(state=NORMAL)

        # Check if the quiz is complete.
        if self.rounds_played.get() >= self.rounds_wanted.get():
            self.question_label.config(text="Quiz Finished! Well Done!")
            self.greek_button.config(state=DISABLED)
            self.roman_button.config(state=DISABLED)
            self.user_choice_label.config(text=f"Your Score: {self.user_score} out of {self.rounds_wanted.get()}")
            return

        # Select a random question for the new round.
        current_question = random.choice(self.all_data)
        # Remove the selected question from the data.
        self.all_data.remove(current_question)

        # Set the question details.
        self.god_name = current_question[2]
        self.correct_answer = current_question[0]

        # Update the UI wih the new question.
        self.god_label.config(text=self.god_name)
        self.choose_heading.config(text=f"Round {self.rounds_played.get() + 1} of {self.rounds_wanted.get()}")

    # Method to check the user's answer.
    def check_answer(self, user_answer):
        # Update the score if the answer is correct.
        if user_answer.lower() == self.correct_answer.lower():
            self.user_score += 1
            self.user_choice_label.config(text="Well done! That's the correct answer! \n"
                                               f"{self.god_name} is {self.correct_answer}.",
                                          bg="#dce3de", width=28, fg="#000000")
            self.round_results_label.config(
                text=f"Round {self.rounds_played.get() + 1}: Current score: {self.user_score}")

        else:
            self.user_choice_label.config(text="Oh no! That answer is incorrect! \n"
                                               f"{self.god_name} is {self.correct_answer}.",
                                          bg="#dce3de", width=28, fg="#000000")
            self.round_results_label.config(
                text=f"Round {self.rounds_played.get() + 1}: Current score: {self.user_score}")

        # Update the rounds played and enable the next button.
        self.rounds_played.set(self.rounds_played.get() + 1)
        self.next_button.config(state=NORMAL)
        self.greek_button.config(state=DISABLED)
        self.roman_button.config(state=DISABLED)

    # Static method for displaying help.
    def get_help(self):
        DisplayHelp(self)

    # Method to close the quiz window.
    def close_quiz(self):
        # reshow root (ie: choose rounds) and end current
        # game / allow new game to start
        root.deiconify()
        self.quiz_box.destroy()


# Help class - this is where the help information is located and displayed
class DisplayHelp:
    def __init__(self, partner):
        # setup dialogue box and background colour
        background = "#FFFFFF"
        self.help_box = Toplevel()

        # disable help button
        partner.help_button.config(state=DISABLED)

        # If users press cross at top, closes help and
        # 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=500,
                                height=400,
                                bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        bg=background,
                                        text="HELP / INFO",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        # help text
        help_text = ""

        self.help_text_label = Label(self.help_frame, bg=background,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="DISMISS", bg="#dce3de",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help,
                                                     partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    # closes help dialogue (used by button and x at top of dialogue)
    def close_help(self, partner):
        # Put help button back to normal...

        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Gods Quiz")
    ChooseRounds()
    root.mainloop()