from flask import *


from backend.api.auth import create_account
'''
To run, use *flask run*
Later, this command will need to be different in order for the server to be reachable

database only = docker-compose -f docker-compose.db.yml up
both = docker compose up --build
'''

app = Flask(__name__)




@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/register')
def register():
    response = make_response(render_template("register.html"))
    return response

@app.route('/register_data', methods = ['POST'])
def register_new():
    response = create_account(request)
    return response