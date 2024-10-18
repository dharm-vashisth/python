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
    print("List Comprehension")
    print('Even numbers under 100 using list comprehension method are shown below')
    print(_number_list, end='\n\n')

    # set comprehension
    _random_list = ['value ' + str(a) for a in range(len(_number_list))]
    print("Set Comprehension")
    _my_set = {i for i in _random_list}
    print(_my_set, end='\n\n')


    #dictionary comprehension
    print("Dictionary Comprehension")
    _my_dict = {(i,j) for i in _number_list  for j in _random_list}
    print(_my_dict, end='\n\n')


if __name__ == "__main__":
    main()
