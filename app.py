import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']

    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']

    return 'I am waving at ' + name

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    vowels = len([char for char in text if char.lower() in 'aeiou'])
    # for char in text:
    #     if char.lower() in 'aeiou':
    #         vowels += 1
    return f'There are {vowels} vowels in "{text}"'


@app.route('/sort-names', methods=['POST'])
def sort_names():
    names = request.form['names']
    return ','.join(sorted(names.split(',')))


@app.route('/names', methods=['GET'])
def names_add():
    name_list = ['Julia', 'Alice', 'Karim']
    names_string = request.args['add']
    names = names_string.split(',')
    name_list.extend(names)
    return ', '.join(name_list)



# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'

    # Send back a friendly greeting with the name
    return f"Hello {name}!"


@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

