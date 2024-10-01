# @author: Dharm Vashisth
# @date: 2024-10-02
# @title: Guess the magical number game
# @description: Try your luck in guessing the game between 0-9.
# @extra: First Milestone!!!
# @Version: 1.0
from random import random


def get_lucky_number():
    return int((random() * 100) // 10)


def get_result_with_announcement(guess_number):
    _lucky_number = get_lucky_number()
    if guess_number == _lucky_number:
        print("You Won to guess the lucky number")

    else:
        print(f"Lucky number is {_lucky_number}.")
        print("Better luck next time :)")


def start_the_game():
    print("\nWelcome to the magical number game:", end='\n\n')
    guess_number = int(input("Guess the number from 0 to 9: "))
    print("\nResult:")
    get_result_with_announcement(guess_number)


start_the_game()
