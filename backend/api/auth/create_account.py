from flask import *
import html
import validate_password
from dotenv import load_dotenv
import os
import bcrypt
import secrets
import hashlib

from psycopg import connect, errors

load_dotenv()

def create_account(request : Request):

    data = request.get_json()

    username = data['username']
    username = html.escape(username)
    password = data['password']
    email = data['email']

    if not validate_password(password):
        return make_response('Invalid Password', 400)

    conn = connect(os.getenv('DATABASE_URL'))
    curr = conn.cursor()


    
    try:
        curr.execute(
            'INSERT INTO users (username, email, hashed_pw) VALUES (%s, %s, %s)', 
            (username, email, bcrypt.hashpw(password.encode(), bcrypt.gensalt()))
        )
        conn.commit()


    except errors.UniqueViolation as e:
        if e.diag.constraint_name == 'unique_username' :
            return make_response('Username already exists', 400)
        elif e.diag.constraint_name == 'unique_email':
            return make_response('Email already exists', 400)
        else:
            return make_response('Error Creating Account', 400)
    finally:
        curr.close()
        conn.close()

    return make_response({'message': 'Account Created Sucessfully'}, 201)