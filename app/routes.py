from app import app, db
from app.models import Topic
from flask import render_template, redirect, request
import random

@app.route('/')
def index():
    topics = Topic.query.all()
    return render_template('index.html', title='Home', topics=topics)

@app.route('/', methods=['POST'])
def create_topic():
    question = request.form['question']
    answer = request.form['answer']
    newTopic = Topic(question=question, answer=answer)
    db.session.add(newTopic)
    db.session.commit()
    return redirect('/')

# an attempt to create a filter method
# @app.route('/')
# def search_results(search):
#     results = []
#     search_string = search.data['search']
#     if search_string:
#         if search.data['select'] == 'answer':
#             qry = db_session.query(Topic).filter(
#                     Topic.answer.contains(search_string))
#             results = [item[0] for item in qry.all()]
#         elif search.data['select'] == 'question':
#             qry = db_session.query(Topic).filter(
#                 Topic.question.contains(search_string))
#             results = qry.all()
#         else:
#             qry = db_session.query(Topic)
#             results = qry.all()
#     else:
#         qry = db_session.query(Topic)
#         results = qry.all()
#     if not results:
#         print('No results found!')
#         return redirect('/')
#     else:
#         # display results
#         table = Results(results)
#         table.border = True
#         return render_template('index.html', table=table)


# @app.route('/random_quiz')
# def random_quiz_home():
#     topics = Topic.query.all()
#     return render_template('random_quiz.html', title='Random Quiz', topics=topics)

@app.route('/random_quiz')
def create_quiz():
    topics = Topic.query.all()
    quiz = random.sample(topics, k=4)
    return render_template('random_quiz.html', quiz=quiz, topics=topics)