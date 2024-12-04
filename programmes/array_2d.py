# --------------------------------------------------
#  ____    __      __
# |  _ \   \ \    / /
# | | | |   \ \  / /
# | | | |    \ \/ /
# | |_| |     \  /
# |____/       \/
# --------------------------------------------------
# Author      : Dharm Vashisth
# Created on  : 2024-12-04
# Description : 2D array access
#
# --------------------------------------------------


# Class and sections - [[1A,1B,2C],[2A,2B,C],[3A,3B,3C],[4A,4B,4C]]
class_size = [[25, 30, 28],
              [20, 22, 25],
              [27, 24, 26],
              [18, 20, 22]]

section_index = {
    'A': 1, 'B': 2, 'C': 3
}


def total_student_in_class(class_name):
    error_message = 'Invalid class name. please ensure the classes should be in range [1A ... 4C]'

    if len(class_name) != 2:
        print(error_message)

    else:
        class_number = int(class_name[0])
        section = class_name[1].upper()
        if (class_number < 1 or class_number > 4) or (section < 'A' or section > 'D'):
            print(error_message)
        else:
            print(
                f"Total Students in class {class_number}{section} is {class_size[class_number - 1][section_index[section] - 1]}")


def main():
    my_class = input('Enter the class[1-4] and section[A-C]:')
    total_student_in_class(my_class)


if __name__ == '__main__':
    main()
