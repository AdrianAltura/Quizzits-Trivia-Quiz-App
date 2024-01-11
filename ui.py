from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 18, 'italic')


class QuizzerInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzits')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text='test',
            fill=THEME_COLOR,
            font=FONT,
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=25)

        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')

        self.true_button = Button(image=true_img, highlightthickness=0, command=self.is_true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_img, highlightthickness=0, command=self.is_false)
        self.false_button.grid(row=2, column=1)

        self.score_label = Label(text=f'Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            new_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=new_text)
        else:
            self.canvas.itemconfig(self.question_text, text='End of the Quiz!')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def is_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def is_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, correct):
        if correct:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
