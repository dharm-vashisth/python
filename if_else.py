# -------------------------------------------------- 
#  ____    __      __                                
# |  _ \   \ \    / /                                
# | | | |   \ \  / /                                 
# | | | |    \ \/ /                                  
# | |_| |     \  /                                   
# |____/       \/                                    
# -------------------------------------------------- 
# Author      : Dharm Vashisth  
# Created on  : 2024-10-23
# Description : if else
#                                                    
# -------------------------------------------------- 


def main():
    try:
        number = int(input("Enter a number"))
        if number % 2 == 0:
            print("Even number")
        else:
            print("Odd number")

    except Exception as e:
        print("Got exception while reading a number. Exception: ",e)


if __name__ == "__main__":
    main()
