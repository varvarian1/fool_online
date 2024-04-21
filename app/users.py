import json
import random
import string
from flask import request, jsonify
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
        return jsonify({
            'id': new_user.id, 
            'email': new_user.email, 
            'username': new_user.username, 
            'password': new_user.password 
        }), 201

   
    
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
            'room_id': user.room_id
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
    
    return jsonify({
        'id': user.id, 
        'email': user.email, 
        'username': user.username, 
        'password': user.password 
    })

@app.route("/users/changeUsername", methods=['PATCH'])
def changeUsername():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'no body'})
    
    userId = data['userId']
    username = data['username']

    user = Users.query.filter_by(id=userId)
    user.update({'username': username})
    db.session.commit()
    
    userEnitity = user.first()
    return jsonify({
        'id': userEnitity.id, 
        'email': userEnitity.email, 
        'username': userEnitity.username, 
        'password': userEnitity.password 
    })

@app.route("/users/deleteAll", methods=['DELETE'])
def deleteAllUsers():
	Users.query.delete()
	db.session.commit()
	return jsonify({'message': 'deleted'})

@app.route("/users/deleteById", methods=['DELETE'])
def deleteUserById():
    data = request.get_json()

    if not data:
        return jsonify({'message': 'no body'}), 400
    
    userId = data['userId']
    Users.query.filter_by(id=userId).delete()

    db.session.commit()
    return jsonify({'message': 'User successfuly deleted'})
