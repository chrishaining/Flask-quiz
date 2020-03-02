from app import app, db
from app.models import Topic, Resource 
from flask import render_template, redirect, request
import random
from sqlalchemy import update

@app.route('/manage')
def manage():
    topics = Topic.query.all()
    return render_template('manage.html', title='Manage', topics=topics)

@app.route('/manage', methods=['POST'])
def create_topic():
    question = request.form['question']
    answer = request.form['answer']
    newTopic = Topic(question=question, answer=answer)
    db.session.add(newTopic)
    db.session.commit()
    return redirect('/manage')

# update a topic. This works. 
@app.route('/manage/<int:topic_id>/update_answer', methods=['POST'])
def update_answer(topic_id):
    newanswer = request.form.get("newanswer")
    topic_id = request.form.get("topic_id")
    topic = Topic.query.filter_by(id=topic_id).first()
    topic.answer = newanswer
    db.session.commit()
    return redirect('/manage')

@app.route('/manage/<int:topic_id>/update_question', methods=['POST'])
def update_topic(topic_id):
    newquestion = request.form.get("newquestion")
    topic_id = request.form.get("topic_id")
    topic = Topic.query.filter_by(id=topic_id).first()
    topic.question = newquestion
    db.session.commit()
    return redirect('/manage')

@app.route('/quiz')
def show_quiz():
    quiz = Topic.query.all()
    score=0
    for topic in quiz:
        # topic.check_answer()
        if topic.answer == topic.user_answer:
        # if topic.points == 1:
            score +=1
            # topic.points = 1
    
    return render_template('quiz.html', title='Quiz', quiz=quiz, score=score)

# answer a question. 
@app.route('/quiz/<int:topic_id>/answer', methods=['POST'])
def answer_question(topic_id):
    new_user_answer = request.form.get("new_user_answer")
    topic_id = request.form.get("topic_id")
    topic = Topic.query.filter_by(id=topic_id).first()
    topic.user_answer = new_user_answer
    db.session.commit()
    return redirect('/quiz')

# flipcard fun
@app.route('/home')
def flipper():
    topics = Topic.query.all()
    card = random.choice(topics)
    return render_template('home.html', title='Home', topics=topics, card=card)

# create a further resources page for links to relevant websites
@app.route('/further_resources')
def show_further_resources():
    resources = Resource.query.all()
    return render_template('further_resources.html', title='Further Resources', resources=resources)

# Add a url - but to do this, I might need a model
@app.route('/further_resources', methods=["POST"])
def add_url():
    new_url = request.form['new_url']
    new_title = request.form['new_title']
    new_resource = Resource(url=new_url, title=new_title)
    db.session.add(new_resource)
    db.session.commit()
    return redirect('/further_resources')



