from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Store the random number in a global variable for simplicity
random_number = random.randint(1, 50)
attempts = 5

@app.route('/')
def index():
    global attempts
    return render_template('index.html', attempts=attempts)

@app.route('/guess', methods=['POST'])
def guess():
    global random_number, attempts

    # Get the guess from the form
    guess = int(request.form['guess'])
    message = ""
    
    if guess > random_number:
        message = "Wrong guess, try a smaller number."
    elif guess < random_number:
        message = "Wrong guess, try a greater number."
    else:
        message = "Yahoo! You won!"

    attempts -= 1
    
    if attempts == 0 and guess != random_number:
        message = f"Game Over! The number was {random_number}."

    return render_template('index.html', attempts=attempts, message=message)

if __name__ == '__main__':
    app.run(debug=True)
