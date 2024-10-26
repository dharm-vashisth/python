# -------------------------------------------------- 
#  ____    __      __                                
# |  _ \   \ \    / /                                
# | | | |   \ \  / /                                 
# | | | |    \ \/ /                                  
# | |_| |     \  /                                   
# |____/       \/                                    
# -------------------------------------------------- 
# Author      : Dharm Vashisth  
# Created on  : 2024-10-19      
# Description : Armstrong
#                                                    
# -------------------------------------------------- 


def is_armstrong(n) -> bool:
    tmp_number = n
    result_number = 0
    while tmp_number > 0:
        result_number += (tmp_number % 10) ** 3
        tmp_number //= 10
    return result_number == n


def main():
    _number = int(input('How many armstrong numbers do you want to print?\n'))
    i = 1
    while _number > 0:
        if is_armstrong(i):
            print(i, end=' ')
            _number -= 1
        i += 1


if __name__ == "__main__":
    main()
