from flask import Flask


'''
To run, use *flask run*
Later, this command will need to be different in order for the server to be reachable
'''

app = Flask(__name__)




@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"

