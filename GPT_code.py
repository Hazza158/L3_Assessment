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
            if num_rounds < 1 or num_rounds > 100:
                raise ValueError
        except ValueError:
            # Show an error message if input is not valid
            error_label = Label(self.intro_frame, text="Please enter a valid number of rounds (1-100).", fg="red")
            error_label.grid(row=4, columnspan=2)
            return

        # Start the quiz
        self.to_play(num_rounds)

    def to_play(self, num_rounds):
        Play(num_rounds)

        # Hide root window (i.e., hide rounds choice window).
        root.withdraw()
