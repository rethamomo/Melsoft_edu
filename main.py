# main.py
from flask import Flask, render_template, request, redirect, url_for, session
# from speechd_config import question

from API import make_request,greet_user
from quiz import get_responses, calculate_scores
from APS import calculate_APS_score
import os


# Create a Flask application instance
app = Flask(__name__)
app.secret_key = 'supersecretkey'

# # Configure the API keyz

# In-memory user store for demonstration purposes
users = {}

questions = get_responses()

# Define a route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define a route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return "Invalid credentials"
    return render_template('login.html')

# Define a route for the sign-up page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = password
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/assistant', methods=['GET', 'POST'])
def assistant():
    greeting_message = greet_user()  # Renamed variable
    if request.method == 'POST':
        subject = request.form['subject']
        proficiency = request.form['proficiency']
        user_input = request.form['user_input']

        assistant_response = make_request(subject, proficiency, user_input)
        return render_template('assistant.html', assistant_response=assistant_response, greeting=greeting_message)

    return render_template('assistant.html', greeting=greeting_message)

@app.route('/calc_APS_score', methods=['GET', 'POST'])
def calc_APS_score():
    if request.method == 'POST':    
        
        calc_APS_score = calculate_APS_score()

        return render_template("calc_APS_score.html", APS=calc_APS_score)
    
    return render_template('calc_APS_score.html')


@app.route('/start', methods=['GET', 'POST'])
def start_quiz():
    session['answers'] = [None] * len(questions)
    session['current_question'] = 0
    return redirect(url_for('quiz', question_id=0))



@app.route('/quiz/<int:question_id>', methods=['GET', 'POST'])
def quiz(question_id):
    if 'answers' not in session:
        session['answers'] = [None] * len(questions)
    if 'current_question' not in session:
        session['current_question'] = 0

    if question_id >= len(questions):
        return redirect(url_for('result'))  # Redirect to results page if quiz is complete

    question = questions[question_id]

    if request.method == 'POST':
        if 'next' in request.form:
            answer = request.form.get(f'q{question_id+1}')
            if answer is not None:
                session['answers'][question_id] = int(answer)  # Store the selected value
                session['current_question'] += 1
            return redirect(url_for('quiz', question_id=session['current_question']))
        elif 'previous' in request.form:
            session['current_question'] -= 1
            return redirect(url_for('quiz', question_id=session['current_question']))
        elif 'submit' in request.form:
            answer = request.form.get(f'q{question_id+1}')
            if answer is not None:
                session['answers'][question_id] = int(answer)  # Store the selected value
            return redirect(url_for('result'))

    return render_template('quiz.html', question=question, question_id=question_id)


@app.route('/result')
def result():
    responses = session['answers']
    total = len(questions)

    # Replace None values with 0
    responses = [0 if response is None else response for response in responses]

    scores = calculate_scores(responses)
    dominant_style = max(scores, key=scores.get)

    return render_template("result.html", scores=scores, dominant_style=dominant_style)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/active')
def active():
    return render_template('active.html')

@app.route('/reflective')
def reflective():
    return render_template('reflective.html')

@app.route('/theoretical')
def theoretical():
    return render_template('theoretical.html')

@app.route('/practical')
def practical():
    return render_template('practical.html')

@app.route('/combination')
def combination():
    return render_template('combination.html')

if __name__ == '__main__':
    app.run(debug=True)