from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    balance = db.Column(db.Integer, default=0)
    count_deposit = db.Column(db.Integer, default=0) #общая сумма депозитов
    count_withdrawal = db.Column(db.Integer, default=0) #общая сумма выводов

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    numberOfCards = db.Column(db.String(255), nullable=False)
    #добавить one-to-many к пользователям!!! (many users to one room)