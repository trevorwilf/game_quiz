

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        ans = False
        if self.question_number < len(self.question_list):
            ans = True
        return(ans)

    def current_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        get_answer = input(f"Q{self.question_number}: {current_q.text} (T/F)? ")
        self.check_answer(get_answer, current_q.answer)


    def check_answer(self, user_answer, current_q):
        if user_answer.lower() == "t":
            user_answer = "true"
        if user_answer.lower() == "f":
            user_answer = "false"

        if(user_answer.lower() == current_q.lower()):
            self.score += 1
            print("You got it right!")
        else:
            print("Ehhhhhh")

        print(f"current score is: {self.score}")

