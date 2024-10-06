# -------------------------------------------------- #
#  ____    __      __                                #
# |  _ \   \ \    / /                                #
# | | | |   \ \  / /                                 #
# | | | |    \ \/ /                                  #
# | |_| |     \  /                                   #
# |____/       \/                                    #
# -------------------------------------------------- #
# Author      : Dharm Vashisth                       #
# Created on  : 2024-10-06                           #
# Version     : 1.0                                  #
# Description : Sample program to get entry/single   #
#               line string from user.               #
# -------------------------------------------------- #

from tkinter import *
from tkinter import ttk
from tokenize import String

from gui.utils import show_label

user_name = ''

def set_value_from_input(entry):
    global user_name
    user_name = entry.get()
    entry.delete(0, END)
    print(f'User Name: {user_name}')


def main():
    root = Tk()

    title = show_label(root, "Input from User", 16)
    label = show_label(root, "Enter your name:", 10)
    entry = ttk.Entry(root)
    entry.pack()
    button = ttk.Button(root, text="Submit",command= lambda: set_value_from_input(entry))
    button.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
