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
    # user_answer = db.Column(db.Enum(AnswerChoices), default=AnswerChoices.a, nullable=False)
    user_answer = db.Column(db.String(64), default="I do not know.")

    def __repr__(self):
        return '<User {}>'.format(self.question)

class MultipleChoiceTopic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(64), index=True)
    option_a = db.Column(db.String(64))
    option_b = db.Column(db.String(64))
    option_c = db.Column(db.String(64))
    option_d = db.Column(db.String(64), default="I dunno", nullable=True)
    # option_d = db.Column(db.String(64))
    option_d = "I do not know"

    answer = db.Column(db.String(64))
    outcome = db.Column(db.Boolean, default=False)

    user_answer = db.Column(db.String(64), default=option_d, nullable=True)

    def __repr__(self):
        return '<User {}>'.format(self.question)

    def check_answer(self):
        if self.user_answer == self.answer:
            self.outcome = True
        else:
            self.outcome = False
        return self.outcome
