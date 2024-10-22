# -------------------------------------------------- #
#  ____    __      __                                #
# |  _ \   \ \    / /                                #
# | | | |   \ \  / /                                 #
# | | | |    \ \/ /                                  #
# | |_| |     \  /                                   #
# |____/       \/                                    #
# -------------------------------------------------- #
# Author      : Dharm Vashisth                       #
# Created on  : 2024-10-13                           #
# Description : Objects                              #
#                                                    #
# -------------------------------------------------- #
from classes import (
    Number,
    Dog,
    Voice,
)



def main():
    number = Number(13.4)
    print(number)
    number = Number(24)
    print(number)
    number = Number(12.42e-14)
    print(number)
    number = Number(12.42e14)
    print(number, end='\n\n')
    # throw exception if number is neither integer nor float.
    # number2 = Number("23.4")

    # inheritance
    voice = Voice("Bob")
    voice.voice()
    print(voice, end ='\n\n')

    dog = Dog("Zimmy")
    dog.voice()
    print(dog, end='\n\n')


if __name__ == "__main__":
    main()
