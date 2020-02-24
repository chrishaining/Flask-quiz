from app import db
from app.models import Topic, AnswerChoices


Topic.query.delete()

topic1 = Topic(question="What is the time?", answer='Now')

db.session.add(topic1)
db.session.commit()

timey = Topic.query.all()
print(timey)