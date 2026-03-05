from flask import *
import html
from dotenv import load_dotenv
import os
import bcrypt
import secrets
import hashlib
from psycopg import *

load_dotenv()

def logout(request : Request):

    # Check auth token is valid, if not Bad request, if valid then destroy token

    data = request.get_json()

    if not data or 'auth_token' not in data:
        return make_response('Bad Request', 400)

    auth_token = data['auth_token']
    hashed_token = hashlib.sha256(auth_token.encode()).hexdigest()

    conn = connect(os.getenv('DATABASE_URL'))
    curr = conn.cursor()


    curr.execute(
        'SELECT * FROM users WHERE auth_token = %s',
        (hashed_token,)
    )

    row = curr.fetchone()
    if not row:
        return make_response('Bad Request', 400)
    

    username = row[1]
    curr.execute(
        'UPDATE users set auth_token = NULL WHERE username = %s',
        (username,)
    )

    conn.commit()
    curr.close()
    conn.close()

    res = make_response('Found', 302)
    res.headers['Location'] = '/'

    return res