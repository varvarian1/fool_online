from flask import request, jsonify
from sqlalchemy import update
from app.models import Room, Users, db
from app.game import Game
from app import app

	
def setTrumpCard(self) -> None:
		# TODO: определение козырной карты
		return 

class Player(Users):
	def setCards(self, cards):
		self.cards = cards
		
	def __init__(self, user) -> None:
		self.user = user
		self.cards = []


@app.route('/rooms/createRoom', methods=['POST'])
def createRoom():
	data = request.get_json()
	if data is None:
		return jsonify({'message': 'No body'}), 400
	
	roomName = data['roomName']
	createrEmail = data['createrEmail'] #с фронта посылаем запрос и передаем email создателя комнаты
	numberOfCards = data['numberOfCards']

	if Room.query.filter_by(name=roomName).first():
		return jsonify({'message': 'Room already exists'}), 409

	if roomName is None or createrEmail is None or numberOfCards is None:
		return jsonify({'message': 'Укажите все данные'}), 400


	newRoom = Room(name=roomName, numberOfCards=numberOfCards)
	db.session.add(newRoom)

	createdRoom = Room.query.filter_by(name=roomName).first()
	Users.query.filter_by(email=createrEmail).update({'room_id': createdRoom.id})

	db.session.commit()
	return jsonify({
		'id': createdRoom.id,
		'name': createdRoom.name,
		'numberOfCards': createdRoom.numberOfCards,
	}), 200


@app.route('/rooms/joinToRoom', methods=['POST'])
def joinToRoom():
	data = request.get_json()
	if not data:
		return jsonify({'message': 'invalid body'}), 400
	
	roomId = data['roomId']
	userEmail = data['userEmail']

	room = Room.query.filter_by(id=roomId).first()
	Users.query.filter_by(email=userEmail).update({'room_id': room.id})

	db.session.commit()

	updatedRoom = Room.query.filter_by(id=roomId).first()

	room_users = []
	for user in updatedRoom.users:
		room_users.append({
			'id': user.id,
			'email': user.email,
		})
	res = {
		'id': updatedRoom.id,
		'name': updatedRoom.name,
		'numberOfCards': updatedRoom.numberOfCards,
	}
	res.update({'users': room_users})
	return jsonify(res), 200
  
	#game = Game("room_name") # позже введем такую переменную
	#game.play() # Сам запуск игры
	#return jsonify({'message': 'пользователь успешно присоединился!'}), 200

@app.route('/rooms/getRooms', methods=['GET'])
def getRooms():
	rooms = Room.query.all()
	rooms_list = []

	for room in rooms:
		room_users = []
		for user in room.users:
			room_users.append({
				'id': user.id,
				'email': user.email,
			})
		room_data = {
			'id': room.id,
			'name': room.name,
			'numberOfCards': room.numberOfCards,
		}
		room_data.update({'users': room_users})
		rooms_list.append(room_data)
	return jsonify(rooms_list), 200

@app.route("/rooms/deleteAll", methods=['DELETE'])
def deleteAllRooms():
	rooms = Room.query.all()
	for room in rooms:
		deleteRoom(room.id)
	return jsonify({'message': 'deleted'})

@app.route("/rooms/deleteById", methods=['DELETE'])
def deleteRoomById():
	data = request.get_json()
	if not data:
		return jsonify({'message': 'invalid body'}), 400
	
	roomId = data['roomId']
	deleteRoom(roomId)
	return jsonify({'message': 'Room successfuly deleted'}), 200

def deleteRoom(roomId):
	room = Room.query.filter_by(id=roomId).first()

	users = room.users
	for user in users:
		Users.query.filter_by(email=user.email).update({'room_id': None})

	Room.query.filter_by(id=roomId).delete()

	db.session.commit()