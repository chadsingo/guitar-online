from flask import *
import html
from dotenv import load_dotenv
import os
import bcrypt
import secrets
import hashlib
from psycopg import *

load_dotenv()


def login(request : Request):
    password_col = 3        # Database column with password stored. This is done to avoid hardcoding in case of a database restructure.

    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return make_response('Bad Request', 400)

    username = data['username']
    username = html.escape(username)
    password = data['password'].encode()

    conn = connect(os.getenv('DATABASE_URL'))
    curr = conn.cursor()

    curr.execute(
        'SELECT * FROM users WHERE username = %s', (username,)
    )
    row = curr.fetchone()

    if not row:
        return make_response('Bad Request', 'Incorrect Username or Password', 400)
    
    hashed_pw = row[password_col]

    check = bcrypt.checkpw(password, hashed_pw)

    if check:
        auth_token = secrets.token_hex()
        hashed_token = hashlib.sha256(auth_token.encode()).hexdigest()

        curr.execute(
            'UPDATE users SET auth_token = %s WHERE username = %s',
            (hashed_token, username)
        )

        conn.commit()
        curr.close()
        conn.close()

        res = make_response()
        res.set_cookie('auth_token', auth_token, httponly=True, secure=True, samesite="Strict", )
        # res.headers['X-Content-Type-Options'] = 'nosniff'

        return res
    else:
        curr.close()
        conn.close()

        return make_response('Bad Request', 'Incorrect Username or Password', 400)