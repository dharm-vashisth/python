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
        number = int(input("Enter an integer number"))
        print("Number entered by you is ",number)
    except ValueError as ve:
        print("Got the value error!!!\n",ve)
    except Exception as e:
        print("Exception caught!!!\nError message: ",e)


if __name__ == "__main__":
    main()
