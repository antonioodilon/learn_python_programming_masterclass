# A small function using a card game blackjack game. I didn't write any tkinter
# code, because as far as I know Django is better than tkinter. I intend to
# start learning Django after I finish this course. I took this opportunity
# to review a few useful things from dictionaries and lists

import random


def blackjack() -> tuple:
    """
    This function gets the values from the `suits` list and combines them
    with the values from the `numbers` list, thus creating a dictionary called
    `numbers_suits_cards`. It does the same for the `face_cards`, creating a
    dictionary called `numbers_face_cards`.

    :return: tuple
    """
    suits = ["heart", "diamond", "clubs", "spades"]
    face_cards = ["queen", "king", "jack"]
    numbers = list(range(1, 5))

    numbers_suits_cards = dict(zip(numbers, suits))
    numbers_face_cards = dict(zip(numbers, face_cards))

    return numbers_suits_cards, numbers_face_cards


print(blackjack())
numbers_suits_cards_user, numbers_face_cards_user = blackjack()
print(numbers_suits_cards_user)
print(numbers_face_cards_user)


# Everything below this line were previous attempts to write the function


# def blackjack_2(*args) -> tuple:
#     """
#     This function gets the values from the `suits` list and combines them
#     with the values from the `numbers` list, thus creating a dictionary called
#     `numbers_suits_cards`. It does the same for the `face_cards`, creating a
#     dictionary called `numbers_face_cards`.
#
#     :return: tuple
#     """
#     suits = []
#     face_cards = []
#     numbers = []
#     user_input = input("Please type in the name of the suit cards you want")
#     for arg in args:
#         suits.append(arg)
#         face_cards.append(arg)
#         numbers.append(int(arg))
#     user_input = args
#
#     numbers_suits_cards = dict(zip(numbers, suits))
#     numbers_face_cards = dict(zip(numbers, face_cards))
#
#     return numbers_suits_cards, numbers_face_cards


# numbers_suits_cards_user = dict()
# # numbers_face_cards_user = dict()
# blackjack(numbers_suits_cards_user)
#
# suits2 = ["heart", "diamond", "clubs", "spades"]
# numbers2 = list(range(1, 8))
#
# suits4 = dict(zip(suits2, numbers2))
# print(suits4)

# suits4 = []
#
# for suits, numbers3 in zip(suits2, numbers2):
#     suits4.append([suits, numbers3])
#     # suits4.append(suits)
#
# print(dict(suits4))
# print(suits4)
    # print(suits, numbers3)


# def blackjack():
#
    # numbers_suits_cards = {}
    # numbers_face_cards = dict(numbers_face_cards)

    # for card in numbers:
    #     numbers_suits_cards = zip(numbers, suits)
    # numbers_suits_cards[card] = enumerate(suits)

    # for suit in suits:
    #     for card in numbers:
    #         numbers_suits_cards[suit] = card

    # for face in face_cards:
    #     for card in range(1, 11):
    #         face_cards[face] = card
    #
    # print(numbers_face_cards)