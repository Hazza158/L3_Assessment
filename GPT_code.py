import tkinter as tk
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        # List of possible answers
        self.answers = ["Answer 1", "Answer 2", "Answer 3", "Answer 4"]

        # Create a label to display the question
        self.question_label = tk.Label(root, text="Select the correct answer:")
        self.question_label.pack()

        # Create a frame for buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        # Create buttons
        self.buttons = []
        for i in range(4):
            button = tk.Button(self.button_frame, text=f"Button {i+1}", command=lambda i=i: self.check_answer(i))
            button.grid(row=i//2, column=i%2)
            self.buttons.append(button)

        # Generate the question
        self.generate_question()

    def generate_question(self):
        # Select the correct answer index
        self.correct_index = random.randint(0, 3)

        # Shuffle the answers and assign to buttons
        shuffled_answers = self.answers[:]
        random.shuffle(shuffled_answers)

        for i in range(4):
            self.buttons[i].config(text=shuffled_answers[i])

    def check_answer(self, index):
        if index == self.correct_index:
            tk.messagebox.showinfo("Result", "Correct!")
        else:
            tk.messagebox.showinfo("Result", "Incorrect. Try again!")


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

