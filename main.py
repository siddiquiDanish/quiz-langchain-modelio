
from Quiz import Quiz

my_topic = input("Enter you Topic for Quiz :")
quiz_bot = Quiz()
question = quiz_bot.create_quiz_question(topic=my_topic)
print(question)

ai_answer = quiz_bot.get_openAI_answer(question)
print(ai_answer)

user_answer = quiz_bot.get_human_answer(question)
print(user_answer)

quiz_bot.check_user_guess(user_answer,ai_answer)