from app import db
# from sqlalchemy_utils import URLType
# from furl import furl

# create a topic class. Another option would be to create different classes for parts (e.g. a question class, an answer class). I'm not sure how that would work, and I'd prefer to see how it goes with only one class.
class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(64), index=True)
    answer = db.Column(db.String(64))
    user_answer = db.Column(db.String(64), default="I do not know.")
    unit = db.Column(db.String(8))
    page = db.Column(db.String(100))

    def __repr__(self):
        return '<Topic {}>'.format(self.question)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    # url = db.Column(URLType) This isn't working. I get the message: ModuleNotFoundError: No module named 'sqlalchemy_utils'
    url = db.Column(db.String(64)) #workaround to deal with the utils problem
  
    def __repr__(self):
        return '<Resource {}>'.format(self.title)

  