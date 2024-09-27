from flask import Flask, render_template, request, redirect, url_for, session

# Create a Flask application instance
app = Flask(__name__)
app.secret_key = 'supersecretkey'

# In-memory user store for demonstration purposes
users = {}

# Define a route for the home page
@app.route('/')
def home():
    return "Welcome to the Flask App!"

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


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)