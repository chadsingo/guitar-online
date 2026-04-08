from flask import *
import html
from .validate_password import validate_password
from dotenv import load_dotenv
import os
import bcrypt
import secrets
import hashlib

from psycopg2 import connect, errors

load_dotenv()

def create_account(request : Request):

    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data or 'email' not in data:
        return jsonify({'message': 'Bad Request'}), 400

    username = data['username']
    username = html.escape(username)
    password = data['password']
    email = data['email']

    if not validate_password(password):
        return jsonify({'message': 'Invalid Password'}), 400

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
            return jsonify({'message': 'An Account with that Username Already Exists'}), 400
        elif e.diag.constraint_name == 'unique_email':
            return jsonify({'message': 'An Account with that Email Already Exists'}), 400
        else:
            return jsonify({'message': 'Error Creating Account'}), 400
    finally:
        curr.close()
        conn.close()

    return jsonify({'message': 'Account Created Sucessfully'}), 201