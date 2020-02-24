from app import db
from app.models import Topic, AnswerChoices, MultipleChoiceTopic


Topic.query.delete()
MultipleChoiceTopic.query.delete()

topic1 = Topic(question="What is the time?", answer='Now')
topic2 = Topic(question="What is the date?", answer='Today')
topic3 = Topic(question="What is the year?", answer='This year')


mult_choice1 = MultipleChoiceTopic(question="What is the time?", answer='Now', option_a="Then", option_b="Soon", option_c="Now", user_answer="Now")
mult_choice2 = MultipleChoiceTopic(question="What is the date?", answer='Today', option_a="Yesterday", option_b="Today", option_c="Tomorrow")
mult_choice3 = MultipleChoiceTopic(question="What is the year?", answer='This year', option_a="Last year", option_b="This year", option_c="Next year")


db.session.add(topic1)
db.session.add(topic2)
db.session.add(topic3)
db.session.commit()


db.session.add(mult_choice1)
db.session.add(mult_choice2)
db.session.add(mult_choice3)
db.session.commit()

timey = Topic.query.all()
print(timey)

mults = MultipleChoiceTopic.query.all()
print(mults[0].option_d)
my_answer = mult_choice1.check_answer()
print(my_answer)
print(mult_choice1.outcome)