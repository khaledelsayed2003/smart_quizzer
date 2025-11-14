from tkinter import *
from core.quiz_brain import QuizBrain
from playsound import playsound

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
        if self.quiz.still_has_questions():
            self.canvas.config(bg="#FFFFFF")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text, text= q_text)
        else:
            self.canvas.config(bg="#EE82EE")
            self.canvas.itemconfig(self.ques_text, text=f"You’ve reached the end of the quiz 🎉")
            self.window.after(1, lambda: playsound("smart_quizzer/src/assets/sounds/congrats.mp3")) # success sound played when the user complete the quiz.
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.window.after(5000, self.window.destroy)
    
    
    def true_clicked(self):
        if self.quiz.check_answer("True"):
            self.canvas.config(bg="#00FF00")
        else:
            self.canvas.config(bg="#FF4500")
        self.window.after(1000, self.get_next_question)
    
    
    def false_clicked(self):
        if self.quiz.check_answer("False"):
            self.canvas.config(bg="#00FF00")
        else:
            self.canvas.config(bg="#FF4500")
        self.window.after(1000, self.get_next_question)