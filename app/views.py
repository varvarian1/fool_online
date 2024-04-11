from flask import Flask, g, request, jsonify
from app.models import Users, db
from app import app


@app.route("/")
def main():
    return 'hello'

# registration

@app.route('/register', methods=['POST', 'GET'])
def registration():

    if request.method == 'POST':
            
        data = request.get_json()
        
        email = data['email']
        password = data['password']

        # Checking that a user with this email does not exist
        if Users.query.filter_by(email=email).first():
            return jsonify({'message': 'User already exists'}), 409
            
        # Create a new user
        new_user = Users(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201

    if request.method == 'GET':

        users = Users.query.all()
        user_list = []

        for user in users:
            user_data = {
                'id': user.id,
                'email': user.email,
                'password': user.password
            }
            user_list.append(user_data)
            
        return jsonify(user_list)
    
# login

@app.route("/login", methods=['POST'])
def login():

    data = request.get_json()

    email = data['email']
    password = data['password']
    
    user = Users.query.filter_by(email=email).first()
    
    if not user or user.password != password:
        return jsonify({'message': 'Invalid email or password'}), 401
    
    return jsonify({'message': 'Login successful'})