from flask import *
from flask_cors import CORS

from api.auth.login import login
from api.auth.create_account import create_account
'''
To run, use *flask run*
Later, this command will need to be different in order for the server to be reachable

database only = docker-compose -f docker-compose.db.yml up
both = docker compose up --build
'''

app = Flask(__name__)
CORS(
    app,
    origins="http://localhost:5173",  # use string, not list
    supports_credentials=True,
    allow_headers=["Content-Type"],
    methods=["GET", "POST", "OPTIONS"]
)



@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"

# @app.route('/register')
# def register():
#     response = make_response(render_template("register.html"))
#     return response

@app.route('/register_account', methods = ['POST'])
def register_new():
    response = create_account(request)
    return response

@app.route('/login', methods = ['POST'])
def user_login():
    response = login(request)
    return response