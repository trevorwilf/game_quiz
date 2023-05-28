

from question_model import Question
from data import question_data
from data import QuizData
from quiz_brain import QuizBrain


import requests
import json


quiz_data = QuizData()
question_data = quiz_data.retrieve_questions()

question_bank = []

for entry in question_data:
    question_bank.append(Question(entry["text"], entry["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():

    quiz.current_question()


print("You have completed the score")
print(f"Your score is {quiz.score} / {quiz.question_number}")

