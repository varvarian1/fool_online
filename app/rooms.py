from flask import Flask, g, request, jsonify
from app.models import Users, db
from app import app

#TODO: скорее всего, нужно будет создать класс Game и использовать его уже в логике самой игры


class Room:
	# P.S.
	# * get user from chache on frontend:
	#	AsyncStorage.getItem('@app:session').then(token => {
	#		// use token
	#	});
 
	def __init__(self, roomName, numberOfCards) -> None:
		self.roomName = roomName
		self.participants = [] #players
		self.numberOfCards = numberOfCards

	def setTrumpCard(self) -> None:
		# TODO: определение козырной карты
		return
  

class Player(Users):
	def setCards(self, cards):
		self.cards = cards
		
	def __init__(self, user) -> None:
		self.user = user
		self.cards = []


@app.route('rooms/createRoom', methods=['POST'])
def createRoom():
	data = request.get_json()
	if data is None:
		return jsonify({'message': 'No body'}), 400
	
	roomName = data['roomName']
	createrEmail = data['createrEmail'] #с фронта посылаем запрос и передаем email создателя комнаты
	numberOfCards = data['numberOfCards']

	if roomName is None or createrEmail is None or numberOfCards is None:
		return jsonify({'message': 'Укажите все данные'}), 400


	user = Users.query.filter_by(email=createrEmail).first()
	player = Player(user) #создаем instance игрока на основе пользователя
	newRoom = Room(roomName=roomName, numberOfCards=numberOfCards)
	newRoom.participants.append(player)
	newRoom.setTrumpCard()

	return jsonify({'message': 'Комната была успешно создана!', 'room': newRoom}), 200


@app.route('rooms/joinToRoom', methods=['POST'])
def joinToRoom():
	#логика присоединения к комнате 
	#request: {email: userEmail}
	return jsonify({'message': 'пользователь успешно присоединился!'}), 200

