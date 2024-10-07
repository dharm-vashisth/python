# -------------------------------------------------- #
#  ____    __      __                                #
# |  _ \   \ \    / /                                #
# | | | |   \ \  / /                                 #
# | | | |    \ \/ /                                  #
# | |_| |     \  /                                   #
# |____/       \/                                    #
# -------------------------------------------------- #
# Author      : Dharm Vashisth                       #
# Created on  : 2024-10-07                           #
# Description : Frame programme                      #
#                                                    #
# -------------------------------------------------- #

from tkinter import *
from tkinter import ttk
from gui.utils import show_label


def main():
    root = Tk()

    title = show_label(root, "Frames", 16)

    # Frame 1
    frame1 = ttk.Frame(root,width=200, height=150)
    frame1.pack()
    frame1.config(relief= GROOVE)

    # Label Frame 2
    frame2 = ttk.LabelFrame(root, text="Frame 2",width=200, height=150)
    frame2.pack()
    frame2.config(relief= SOLID)

    button = ttk.Button(frame1, text="I'm inside frame one")
    button2 = ttk.Button(frame2, text= "I'm inside frame two")
    button.pack()
    button2.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
