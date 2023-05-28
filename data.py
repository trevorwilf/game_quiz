import json

import requests

question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
             "you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a "
             "state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

class QuizData:

    def __init__(self):
        question_data = []

    def retrieve_questions(self):
        url = 'https://opentdb.com/api.php?amount=12&difficulty=easy&type=boolean'
        data = requests.get(url)
        data = data.json()
        data = data['results']
        question_filtered = []
        for entry in data:
            str = entry['question']
            str = str.replace('&quot;','').replace('&#039;', '')
            question_data = {
                "text": str,
                "answer": entry['correct_answer']
            }
            question_filtered.append(question_data)

        return(question_filtered)


