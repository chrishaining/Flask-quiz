from app import db
import enum

# create an enum for multiple choice
class AnswerChoices(enum.Enum):
    a = 'A'
    b = 'B'
    c = 'C'

# create a topic class. Another option would be to create different classes for parts (e.g. a question class, an answer class). I'm not sure how that would work, and I'd prefer to see how it goes with only one class.
class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(64), index=True)
    answer = db.Column(db.String(64))
    user_answer = db.Column(db.Enum(AnswerChoices), default=AnswerChoices.a, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.question)

