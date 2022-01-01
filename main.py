""" True / False Game!  """
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Looping to find the questions and answers
question_bank = []
for question in question_data:
   question_text = question["text"]
   question_answer = question["answer"]
   #Adding the new question into our own quesiton bank
   new_question = Question(question_text, question_answer)
   question_bank.append((new_question))

# Asking questions from Question Bank
quiz = QuizBrain(question_bank)

# Run while there is still questions to ask
while quiz.still_has_questions():
   quiz.next_question()

#telling user their final score!
print("You've completed the quiz!")
print(f"Your final score was: {quiz.score} / {quiz.question_number}")

