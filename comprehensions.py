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
# Description : comprehensions                       #
#                                                    #
# -------------------------------------------------- #


def main():
    # list comprehensions
    _number_list = [a for a in range(1,100) if a%2==0 ]
    print('Even numbers under 100 using list comprehension method are shown below', end='\n\n')
    print(_number_list)


if __name__ == "__main__":
    main()
