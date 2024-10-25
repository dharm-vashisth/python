# -------------------------------------------------- 
#  ____    __      __                                
# |  _ \   \ \    / /                                
# | | | |   \ \  / /                                 
# | | | |    \ \/ /                                  
# | |_| |     \  /                                   
# |____/       \/                                    
# -------------------------------------------------- 
# Author      : Dharm Vashisth  
# Created on  : 2024-10-25
# Description : Programme to print first n prime numbers.
#                                                    
# -------------------------------------------------- 

def is_prime(n):
    if n<2:
        return False
    elif n<3:
        return True
    else:
        for i in range(2,(n//2)+1):
            if n%i==0:
                return False
    return True


def main():
    n = int(input("How many prime numbers do you want?\n"))
    print(f'First {n} prime numbers are shown below:')
    i = 2
    while n>0:
        if is_prime(i):
            print(i,end=' ')
            n-=1
        i+=1


if __name__ == "__main__":
    main()
