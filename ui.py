from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.solve = ''
        self.quiz = quiz_brain
        self.window = Tk()
        self.score = 0
        self.window.config(pady=20, padx=20, background=THEME_COLOR)
        self.window.title('Quizzer')
        self.score_label = Label(text=f'Score: {self.score}', fg='white', bg=THEME_COLOR, font=('Ariel', 10, 'bold'))
        self.score_label.grid(row=0, column=1)
        self.main_canvas = Canvas(width=300, height=250, highlightthickness=0, background='white')

        self.q_text = self.main_canvas.create_text(150, 125, text='', fill=THEME_COLOR,
                                                   font=(
                                                       'Ariel', 20, 'italic'), width=280)
        self.main_canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')
        self.true_button = Button(image=true_img, background=THEME_COLOR, highlightthickness=0,
                                  command=self.when_clicked_true)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_img, background=THEME_COLOR, highlightthickness=0,
                                   command=self.when_clicked_false)
        self.false_button.grid(row=2, column=1)
        self.take_next_question()
        self.window.mainloop()

    def take_next_question(self):
        self.main_canvas.config(background='white')
        if self.quiz.still_has_questions():

            new_q_text = self.quiz.next_question()
            self.main_canvas.itemconfig(self.q_text, text=new_q_text)
        else:

            self.main_canvas.itemconfig(self.q_text, text='Questions are over.See you next time mate')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def when_clicked_true(self):
        if self.quiz.check_answer(user_answer='True'):
            self.give_feedback(True)
        else:
            self.give_feedback(False)

    def when_clicked_false(self):
        if self.quiz.check_answer(user_answer='False'):
            self.give_feedback(True)
        else:
            self.give_feedback(False)

    def give_feedback(self, state: bool):

        if state:
            self.score += 1
            self.score_label.config(text=f'Score {self.score}')
            self.main_canvas.config(background='green')
            self.main_canvas.itemconfig(self.q_text, text="You got it mate!... Well Done")

        else:
            self.main_canvas.config(background='red')
            self.main_canvas.itemconfig(self.q_text, text="Oops!.. It doesn't go well")

        self.solve = self.window.after(1000, self.take_next_question)
