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
# Description : Class Template                       #
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
        msg = "\nClass Name: Number"
        msg += f"\nNumber is {self._number}"
        msg += "\nNumber is "
        if self.is_odd_number():
            msg += "odd."
        else:
            msg += "even."
        return msg

class Voice:
    def __init__(self,name):
        self.name = name

    def voice(self):
        print("Parent Voice method is called.")

    def __repr__(self):
        return f"Hi, my name is {self.name}"

# inheritance
class Dog(Voice):
    def __init__(self,name):
        # calling the parent constructor
        super().__init__(name)

    def voice(self):
        print("Dog class Voice method is called.")

    def __repr__(self):
        return f"Hi, my name is {self.name}. I'm a Dog. I used to bark."
