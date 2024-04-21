from flask import Flask, g, request, jsonify
from app.models import Room, Users, db
from . game import Game
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

	if roomName is None or createrEmail is None or numberOfCards is None:
		return jsonify({'message': 'Укажите все данные'}), 400


	user = Users.query.filter_by(email=createrEmail).first()
	newRoom = Room(name=roomName, numberOfCards=numberOfCards)
	#player = Player(user) #создаем instance игрока на основе пользователя
	# newRoom.participants.append(player)
	#newRoom.setTrumpCard()
	db.session.add(newRoom)
	db.session.commit()
	return jsonify({'message': 'Комната была успешно создана!'}), 200

# тут заход в комнату

@app.route('/rooms/joinToRoom', methods=['POST'])
def joinToRoom():
	#логика присоединения к комнате 
	#request: {email: userEmail}

	return jsonify({'message': 'пользователь успешно присоединился!'}), 200

# тут запуск игры 

@app.route('/rooms/joinToRoom/startGame', methods=['POST'])
def startGame():

	# запуск класса Game from geme.py

	game = Game("room_name") # позже введем такую переменную
	game.play() # Сам запуск игры

	return jsonify({'message': 'Game start'}), 200