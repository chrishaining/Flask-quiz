from app import app, db
from app.models import Topic, MultipleChoiceTopic
from flask import render_template, redirect, request
import random
from sqlalchemy import update

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

# update a topic. This works. 
@app.route('/<int:topic_id>/update', methods=['POST'])
def update_topic(topic_id):
    newanswer = request.form.get("newanswer")
    topic_id = request.form.get("topic_id")
    topic = Topic.query.filter_by(id=topic_id).first()
    topic.answer = newanswer
    db.session.commit()
    return redirect('/')


@app.route('/quiz')
def show_quiz():
    quiz = Topic.query.all()
    score=0
    for topic in quiz:
        topic.check_answer()
        # if topic.answer == topic.user_answer:
        if topic.points == 1:
            score +=1
            # topic.points = 1
    return render_template('quiz.html', quiz=quiz, score=score)

# answer a question. 
@app.route('/quiz/<int:topic_id>/answer', methods=['POST'])
def answer_question(topic_id):
    new_user_answer = request.form.get("new_user_answer")
    topic_id = request.form.get("topic_id")
    topic = Topic.query.filter_by(id=topic_id).first()
    topic.user_answer = new_user_answer
    db.session.commit()
    return redirect('/quiz')

# create random quizzes. It might help to have a TopicsBank class (i.e. all the questions) that has a random_quiz method. It would mean I could do less work in the routes. However, I'm not sure about the implications so I will stick with creating random quizzes through the routes. This method calculates the score (it might be better to put the score somewhere else).
@app.route('/random_quiz')
def show_random_quiz():
    multis = MultipleChoiceTopic.query.all()
    length = int(len(multis)/2)
    quiz = random.sample(multis, length)
    score=0
    for topic in quiz:
        if topic.outcome == True:
            score +=1
    return render_template('random_quiz.html', quiz=quiz, multis=multis, score=score)

# @app.route('/random_quiz')
# def score():
#     score = 0
#     return render_template('random_quiz.html', score=score)

@app.route('/random_quiz', methods=['POST'])
def create_multi_choice_topic():
    question = request.form['question']
    option_a = request.form['option_a']
    option_b = request.form['option_b']
    option_c = request.form['option_c']
    answer = request.form['answer']
    newMultiChoiceTopic = MultipleChoiceTopic(question=question, option_a=option_a, option_b=option_b, option_c=option_c, answer=answer)
    db.session.add(newMultiChoiceTopic)
    db.session.commit()
    return redirect('/random_quiz')


# @app.route('/random_quiz/<int:multiple_choice_topic_id>', methods=['GET', 'POST'])
# def submit_answer(multiple_choice_topic_id):
#     multiple_choice_topic = MultipleChoiceTopic.query.get(multiple_choice_topic_id)
#     user_answer = request.form['user_answer']
#     # multiple_choice_topic.user_answer = request.form['user_answer']
#     db.execute("INSERT INTO multiple_choice_topic.user_answer VALUES (?)", [user_answer])
#     db.session.commit()
#     return redirect('/random_quiz')

  
# @app.route('/random_quiz/<int:multiple_choice_topic_id>', methods=['GET', 'POST'])
# def submit_answer(multiple_choice_topic_id):
    # chosen_multiple_choice_topic = MultipleChoiceTopic.query.get(multiple_choice_topic_id)
    # bob = request.form['user_answer']
    # multiple_choice_topic.user_answer = request.form['user_answer']
    # db.execute("INSERT INTO multiple_choice_topic.user_answer VALUES (?)", [user_answer])

    # MultipleChoiceTopic.update().where(MultipleChoiceTopic.c.id==multiple_choice_topic_id).values(user_answer=bob)
    # db.session.commit()
    # return redirect('/random_quiz')

@app.route('/random_quiz/<int:multiple_choice_topic_id>', methods=['GET', 'POST'])
def submit_answer(multiple_choice_topic_id):
    multiple_choice_topic = MultipleChoiceTopic.query.get(multiple_choice_topic_id)
    multiple_choice_topic.user_answer = request.form['user_answer']
    db.session.commit()
    return redirect('/random_quiz')

# answer a multiple_choice_topic. 
@app.route('/random_quiz/<int:multiple_choice_topic_id>/answer', methods=['POST'])
def answer_multi_choice_question(multiple_choice_topic_id):
    new_user_answer = request.form.get("new_user_answer")
    multiple_choice_topic_id = request.form.get("multiple_choice_topic_id")
    multiple_choice_topic = MultipleChoiceTopic.query.filter_by(id=multiple_choice_topic_id).first()
    multiple_choice_topic.answer = new_user_answer
    db.session.commit()
    return redirect('/random_quiz')