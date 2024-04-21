from flask import Flask, g, request, jsonify
from app.models import Users, db
from app import app
import time

class Game:
    def __init__(self, room):
        self.room = room
        # Дополнительная логика и инициализация игры

    def play(self):
        while not self.isGameOver():
            # Логика игрового цикла
            self.makeMoves()
            time.sleep(1)
            print(1)
        
        winner = self.determineWinner()
        self.endGame(winner)
        print(0)

    def isGameOver(self):
        # Логика, определяющая условие окончания игры
        # Например, когда достигнут определенный счет или когда у одного из игроков закончились карты
        return False  # Замените это на свою логику окончания игры

    def makeMoves(self):
        # Логика, связанная с совершением ходов в игре
        # Каждый игрок делает свой ход в соответствии с правилами игры
        pass

    def determineWinner(self):
        # Логика определения победителя
        # Например, по подсчету очков или по выполнению определенного условия
        # Замените это на свою логику определения победителя
        pass

    def endGame(self, winner):
        # Логика завершения игры
        # Объявление победителя и выполнение необходимых действий
        pass

if __name__ == "__main__":
    game = Game("room_name")
    game.play()