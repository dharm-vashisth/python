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
# Description : Class Template for Number            #
#                                                    #
# -------------------------------------------------- #

class Number:
    def __init__(self, value):
        if type(value) not in (int, float):
            raise Exception("Invalid number")
        self._number = value

    def get_number(self):
        return self._number

    def set_number(self, value):
        self._number = value

    def is_odd_number(self):
        return self._number % 2 != 0

    def is_even_number(self):
        return self._number % 2 == 0

    # dunder method to represent object
    def __repr__(self):
        msg = f"Number is {self._number}"
        msg += "\nNumber is "
        if self.is_odd_number():
            msg += "odd."
        else:
            msg += "even."
        return msg


def main():
    number = Number(23.4)
    print(number)
    # throw exception if number is neither integer nor float.
    # number2 = Number("23.4")


if __name__ == "__main__":
    main()