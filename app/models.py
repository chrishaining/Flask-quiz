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
    # links = db.relationship('Link', backref='topic', lazy='dynamic')


    # points = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Topic {}>'.format(self.question)

    # def check_answer(self):
    #     if self.user_answer == self.answer:
    #         self.points = 1
    #     else:
    #         self.points = 0
    #     return self.points

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
        return '<MultipleChoiceTopic {}>'.format(self.question)

    def check_answer(self):
        if self.user_answer == self.answer:
            self.outcome = True
        else:
            self.outcome = False
        return self.outcome

# class Quiz(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     links = db.relationship('Link', backref='quiz', lazy='dynamic')
#     topics = db.relationship('Topic', backref='quiz', lazy='dynamic')
#     quiz_topics = []

#     def __repr__(self):
#         return '<Quiz {}>'.format(self.id)
    
#     def add_topic(self, topic):
#         self.quiz_topics.append(topic)
#         return self.quiz_topics

#     def show_questions(self):
#         for topic in self.quiz_topics:
#             return 'Question {}'.format(topic)

    # create a Link class to connect Topic and Quiz. This means that a Topic will have to have a way to attach multiple quizzes, and a Quiz will have to have a way to attach multiple topics.
# class Link(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
#     quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))



