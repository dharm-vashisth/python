# -------------------------------------------------- #
#  ____    __      __                                #
# |  _ \   \ \    / /                                #
# | | | |   \ \  / /                                 #
# | | | |    \ \/ /                                  #
# | |_| |     \  /                                   #
# |____/       \/                                    #
# -------------------------------------------------- #
# Author      : Dharm Vashisth                       #
# Created on  : 2024-10-18                           #
# Description : Exception Handling                   #
#                                                    #
# -------------------------------------------------- #


def main():
    try:
        number = int(input("Enter an integer number: "))
        print("Number entered by you is ",number)
        number2 = int(input("Enter an integer number 2: "))
        print("Number2 entered by you is ",number2)
        print("Division of number by number 2 is ",number/number2)
    except ZeroDivisionError as ze:
        print("Got the Divisible by Zero exception!!!\n",ze)
    except ValueError as ve:
        print("Got the value error!!!\nNot getting an integer value\n",ve)
    except Exception as e:
        print("Exception caught!!!\nError message: ",e)


if __name__ == "__main__":
    main()
