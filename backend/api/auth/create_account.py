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

def create_account(request : Request):

    data = request.get_json()

    username = data['username']
    username = html.escape(username)
    password = data['password']
    email = data['email']

    conn = connect(os.getenv('DATABASE_URL'))
    curr = conn.cursor()

    curr.execute(
        """SELECT 
        username = %s AS username_exists, email = %s AS email_exists 
        FROM users WHERE username = %s OR email = %s
        """,
        (username, email, username, email)
        )
    
    row = curr.fetchone()

    if row:
        username_exists, email_exists = row

        if username_exists:
            conn.close()
            return make_response(400, 'Username already exists')
        if email_exists:
            conn.close()
            return make_response(400, 'Email already exists')
        

    if not validate_password(password):
        return make_response('Invalid Password', 400)
    
    curr.execute(
        'INSERT INTO users (username, email, hashed_pw) VALUES (%s, %s, %s)', 
        (username, email, bcrypt.hashpw(password.encode(), bcrypt.gensalt()))
    )
    
    conn.commit()
    curr.close()
    conn.close()

    return make_response()