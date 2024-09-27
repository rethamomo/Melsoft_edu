# main.py
from flask import Flask, render_template, request, redirect, url_for, session
from API import make_request,greet_user
import os


# Create a Flask application instance
app = Flask(__name__)
app.secret_key = 'supersecretkey'

# # Configure the API key
# os.environ["GEMINI_API_KEY"] = "AIzaSyDFyfAGt-PRplWy6B-qgk1TCLhBzq2fR1w"

# In-memory user store for demonstration purposes
users = {}

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


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)