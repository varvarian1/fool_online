import random
import string
from flask import Flask, g, request, jsonify
from app.models import Users, db
from app import app


@app.route("/")
def main():
    return 'hello'


def generate_random_string():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))
# registration
@app.route('/register', methods=['POST'])
def registration():

    if request.method == 'POST':
            
        data = request.get_json()
        
        email = data['email']
        password = data['password']


        # Checking that a user with this email does not exist
        if Users.query.filter_by(email=email).first():
            return jsonify({'message': 'User already exists'}), 409
            
        # Create a new user
        username = generate_random_string()
        new_user = Users(email=email, password=password, username=username)


        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201

   
    
@app.route("/getUsers", methods=['GET'])
def getUsers():
    users = Users.query.all()
    user_list = []

    for user in users:
        user_data = {
            'id': user.id,
            'email': user.email,
            'password': user.password,
            'username': user.username,
        }
        user_list.append(user_data)
        
    return jsonify(user_list)


@app.route("/login", methods=['POST'])
def login():

    data = request.get_json()

    email = data['email']
    password = data['password']
    
    user = Users.query.filter_by(email=email).first()
    
    if not user or user.password != password:
        return jsonify({'message': 'Invalid email or password'}), 401
    
    return jsonify({'message': 'Login successful'})