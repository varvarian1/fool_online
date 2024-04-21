#2 lists: 1 - масти 2 - номиналы (у каждого номинала есть каждая возможная масть)
#UPD: нужно несколько массивов, так как количество карт может быть разным

from flask import Flask, jsonify

app = Flask(__name__)

def compareСards(card1, card2):
    """

    Сравнивает две карты и определяет, какая карта бьет другую.
    
    Аргументы:
    card1 (str): Первая карта в формате 'ранг' + 'масть'.
    card2 (str): Вторая карта в формате 'ранг' + 'масть'.
    
    Возвращает:
    str: Результат сравнения карт.

    
    """
    suits = {'C': 'Clubs', 'D': 'Diamonds', 'H': 'Hearts', 'S': 'Spades'} # словарь с обозначением и буквальным названием мастей
    ranks = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14} # словарь для обозначения ранга(числа)

    suit1, rank1 = card1[-1], card1[:-1] # соответствие между первыми suits и ranks
    suit2, rank2 = card2[-1], card2[:-1] # соответствие между вторыми suits и ranks

    if suit1 != suit2:
        return "Cards of different suits cannot be compared." # если разные масти, ШЛЕМ НАХУЙ

    if ranks[rank1] > ranks[rank2]:
        return f"{card1} ({suits[suit1]}) beats {card2} ({suits[suit2]})." # Если ранг карты 1 больше ранга карты 2, возвращаем сообщение о победе карты 1 над картой 2
    
    elif ranks[rank1] < ranks[rank2]:
        return f"{card2} ({suits[suit2]}) beats {card1} ({suits[suit1]})." # Если ранг карты 1 меньше ранга карты 2, возвращаем сообщение о победе карты 2 над картой 1
    
    else:
        return f"{card1} ({suits[suit1]}) and {card2} ({suits[suit2]}) are equal." # Если ранги карт равны, возвращаем сообщение о равенстве карт


card1 = input("Введите первую карту: ")  # ввод 1
card2 = input("Введите вторую карту: ")  # ввод 2

result = compareСards(card1, card2)
print(result)