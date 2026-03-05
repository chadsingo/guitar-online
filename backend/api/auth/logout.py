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
        'UPDATE users set auth_token = NULL WHERE auth_token = %s',
        (hashed_token,)
    )
    
    if curr.rowcount == 0:
        return make_response('Bad Request', 400)

    conn.commit()
    curr.close()
    conn.close()

    res = make_response('Found', 302)
    res.headers['Location'] = '/'

    return res