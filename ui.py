from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

x = 150
y = 125

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial",20, "bold"))
        self.score_label.grid(column=1, row=0)

        self.set= self.canvas = Canvas(width=300, height=250,bg="white")
        self.question_text = self.canvas.create_text(
            x,y,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR ,font=("Arial", 20 ,"italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)

        true_button_photo = PhotoImage(file="./images/true.png")
        self.true_button = Button(
            image=true_button_photo, width=100,
            height=97,border=0,highlightthickness=0,command=self.true_pressed
        )
        self.true_button.grid(column=0 , row=2)

        false_button_photo = PhotoImage(file="./images/false.png")
        self.false_button = Button(
            image=false_button_photo,width=100,
            height=97,border=0,highlightthickness=0,command=self.false_pressed
        )
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # default canvas color
        self.canvas.config(bg="white")
        # check if the question list is still available
        if self.quiz.still_has_questions():
            # show the user feedback
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            is_right =self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            # disable the buttons
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        # Check the answer once and store the result
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        # Check the answer once and store the result
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        # Change the color to green if true
        if is_right:
            self.canvas.config(bg="green")
        # Change the color to red if false
        else:
            self.canvas.config(bg="red")

        # Update the canvas screen after 1000 ms (1 second)
        self.window.after(1000, self.get_next_question)





