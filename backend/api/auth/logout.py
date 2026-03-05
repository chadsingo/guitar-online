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
    auth_token = data['auth_token']

    conn = connect(os.getenv('DATABASE_URL'))
    curr = conn.cursor()

    curr.execute(
        'SELECT * FROM users WHERE auth_token = %s'
        (hashlib.sha256(auth_token.encode()).hexdigest(),)
    )

    row = curr.fetchone()
    if not row:
        return make_response('Bad Request', 400)
    
    curr.execute(
        
    )


    return