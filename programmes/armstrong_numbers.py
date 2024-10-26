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


def is_armstrong(n)-> bool:
    tmp = n
    result = 0
    while tmp>0:
        result+=(tmp%10)**3
        tmp//=10
    return result == n


def main():
    _number=int(input('Enter a number: '))
    if is_armstrong(_number):
        print("Number is armstrong.")
    else:
        print("Number is not an armstrong.")


if __name__ == "__main__":
    main()
