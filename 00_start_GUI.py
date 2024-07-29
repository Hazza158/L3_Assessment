from tkinter import *
from functools import partial  # To prevent unwanted windows


class ChooseRounds:

    def __init__(self):
        button_fg = "#FFFFFF"
        button_font = ("Arial", "13", "bold")

        # Set up GUI Frame
        self.intro_frame = Frame(padx=10, pady=10)
        self.intro_frame.grid()

        # Heading and brief instructions
        self.intro_heading_label = Label(self.intro_frame, text="Greek Gods Quiz",
                                         font=("Arial", "16", "bold"))
        self.intro_heading_label.grid(row=0)

        choose_instructions_txt = "In this quiz you will input the amount of " \
                                  "questions you want to answer, then press the " \
                                  "'START' button to begin the quiz."

        self.choose_instructions_label = Label(self.intro_frame,
                                               text=choose_instructions_txt,
                                               wraplength=300, justify="left")
        self.choose_instructions_label.grid(row=1)

        self.rounds_entry = Entry(self.intro_frame)
        self.rounds_entry.grid(row=2, column=0)

        # Start button to initiate the quiz
        self.start_button = Button(self.intro_frame, text="START",
                                   fg=button_fg, bg="#009900",
                                   font=button_font,
                                   command=self.start_quiz)
        self.start_button.grid(row=3, columnspan=2, pady=10)

    def start_quiz(self):
        try:
            num_rounds = int(self.rounds_entry.get())
            if num_rounds < 1:
                raise ValueError
        except ValueError:
            # Show an error message if input is not valid
            error_label = Label(self.intro_frame, text="Please enter a valid number of rounds.", fg="red")
            error_label.grid(row=4, columnspan=2)
            return

        # Start the quiz
        self.to_play(num_rounds)

    def to_play(self, num_rounds):
        Play(num_rounds)

        # Hide root window (i.e., hide rounds choice window).
        root.withdraw()


class Play:

    def __init__(self, how_many):
        self.play_box = Toplevel()

        # If users press cross at top, close help and
        # 'release' help button
        self.play_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_play))

        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()

        rounds_heading = "Choose - Round 1 of {}".format(how_many)
        self.choose_heading = Label(self.quest_frame, text=rounds_heading,
                                    font=("Arial", "16", "bold"))
        self.choose_heading.grid(row=0)

        self.control_frame = Frame(self.quest_frame)
        self.control_frame.grid(row=6)

        self.start_over_button = Button(self.control_frame, text="Start Over",
                                        command=self.close_play)
        self.start_over_button.grid(row=0, column=2)

    def close_play(self):
        # Reshow root (i.e., choose rounds) and end current
        # game / allow new game to start
        root.deiconify()
        self.play_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Greek Gods Quiz")
    ChooseRounds()
    root.mainloop()
