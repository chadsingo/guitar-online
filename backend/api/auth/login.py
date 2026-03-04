from flask import *
import html
import validate_password
from dotenv import load_dotenv
import os
import bcrypt
import secrets
import hashlib
from psycopg import *

load_dotenv()


def login(request : Request):

    data = request.get_json()

    username = data['username']
    username = html.escape(username)
    password = data['password']

    conn = connect(os.getenv('DATABASE_URL'))
    curr = conn.cursor()

    curr.execute(
        'SELECT * FROM users WHERE username = %s', (username)
    )
    row = curr.fetchone()

    if not row:
        return make_response(400, 'Bad Request', 'Incorrect Username or Password')


    return make_response()