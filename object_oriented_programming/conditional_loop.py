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
# Description : Conditional loop
#
# --------------------------------------------------


def main():
    print('Conditional Loop: Loop will execute unless you provide 0 integer.')
    i=int(input("Provide an integer"))
    while i!=0:
        print("Loop is executing...")
        i = int(input("Provide an integer"))
    print('Loop is terminated!')



if __name__ == "__main__":
    main()
