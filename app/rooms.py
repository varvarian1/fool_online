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


