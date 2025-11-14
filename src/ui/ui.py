from tkinter import *
from core.quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Smart Quizzer")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.score_label = Label(text=f"score: {self.score}", fg="#FFFFFF", bg= THEME_COLOR, font=(FONT_NAME, 20, "italic"))
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=400, height=250, bg="#FFFFFF", highlightthickness=0)
        self.ques_text = self.canvas.create_text(200, 125, width=380, text="starting point!", font=(FONT_NAME, 20, "italic"), fill="#006400")
        self.canvas.grid(row=1, column=0, columnspan=2, sticky="ew", pady=50)
        true_img = PhotoImage(file="smart_quizzer/src/assets/images/true.png")
        self.true_button = Button(image=true_img, command= self.true_clicked, highlightthickness=0, borderwidth=0, activebackground=THEME_COLOR)
        self.true_button.grid(row=2, column=0)
        false_img = PhotoImage(file="smart_quizzer/src/assets/images/false.png")
        self.false_button = Button(image=false_img, command= self.false_clicked, highlightthickness=0, borderwidth=0, activebackground=THEME_COLOR)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()
                
   
   
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.ques_text, text= q_text)
        
    
    def true_clicked(self):
        self.quiz.check_answer("True")
        self.get_next_question()
    
    def false_clicked(self):
        self.quiz.check_answer("False")
        self.get_next_question()