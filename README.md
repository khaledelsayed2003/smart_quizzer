# 🧠 Smart Quizzer

Smart Quizzer is a small Python desktop app built with Tkinter that lets you play a True/False trivia quiz.
Questions are fetched live from the free Open Trivia Database API, and the app shows your score, visual feedback, and a short celebration sound when you finish.

---

## 🚀 Features

- Fetches questions from Open Trivia DB (https://opentdb.com/api.php).

- True/False questions with adjustable:
   - number of questions
   - difficulty
   - type (boolean)

- Simple Tkinter GUI:
   - Score label
   - Question card
   - ✅ / ❌ buttons

- Visual feedback:
   - Green background → correct answer
   - Red background → wrong answer

- End screen:
   - “You’ve reached the end of the quiz 🎉”
   - Plays a success sound (congrats.mp3)
   - Automatically closes after a few seconds

--- 

## 🔧 Requirements

- Install dependencies from requirements.txt:
  - requests – to call the Open Trivia API
  - playsound – to play the completion sound
  - tkinter and html – from the Python standard library (no install needed)

---

## ⚙️ Changing Quiz Settings

- You can change the quiz configuration in src/data/data.py:
    - num_of_questions = 50
    - difficulty = "hard"       # "easy", "medium", or "hard"
    - type_of_questions = "boolean"  # True/False questions


---


## 📜 License
This project is licensed under the MIT License.
See the LICENSE file for more details.


## 💫 Author
Khaled Elsayed (KE)
Developed as part of a Python learning.


---

## 📁 Project Structure
```bash
smart_quizzer/
│
├── src/
│   ├── main.py
│   │
│   ├── assets/
│   │   ├── images/
│   │   │   ├── correct_answer_screen.png
│   │   │   ├── false.png
│   │   │   ├── quiz_completion_screen.png
│   │   │   ├── quiz_start.png
│   │   │   ├── trivia_web.png
│   │   │   ├── true.png
│   │   │   └── wrong_answer_screen.png
│   │   │
│   │   └── sounds/
│   │       └── congrats.mp3
│   │
│   ├── core/
│   │   ├── question_model.py   # Question class
│   │   └── quiz_brain.py       # QuizBrain logic (score, next question, checking answers)
│   │
│   ├── data/
│   │   └── data.py             # Fetches question_data from Open Trivia API
│   │
│   └── ui/
│       └── ui.py               # Tkinter QuizInterface GUI
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt


---