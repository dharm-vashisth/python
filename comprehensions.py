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

    _random_list = ['value '+str(a) for a in range(len(_number_list))]
    print(_random_list)

    #dictionary comprehension
    _my_dict = {(i,j) for i in _number_list  for j in _random_list}
    print(_my_dict)


if __name__ == "__main__":
    main()
