# -------------------------------------------------- #
#  ____    __      __                                #
# |  _ \   \ \    / /                                #
# | | | |   \ \  / /                                 #
# | | | |    \ \/ /                                  #
# | |_| |     \  /                                   #
# |____/       \/                                    #
# -------------------------------------------------- #
# Author      : Dharm Vashisth                       #
# Created on  : 2024-10-08                           #
# Description : Pane Window with Frames              #
#                                                    #
# -------------------------------------------------- #

from tkinter import *
from tkinter import ttk

from PIL.ImageOps import expand

from gui.utils import show_label, show_frame


def main():
    root = Tk()
    root.geometry('500x500+10+20')
    title = show_label(root, "Pane Window", 16)
    label = show_label(root, "Pane containing frames:", 10)

    pane = ttk.Panedwindow(root, orient=HORIZONTAL)
    pane.pack(fill= BOTH, expand= True, padx=20, pady=20,)

    frame1 = show_frame(root, 200, 500)
    frame_label1 = show_label(frame1, "Left Frame", 12)
    frame_label1.config(relief= GROOVE,background='lightblue', padding=(20,5))

    frame2 = show_frame(root, 400, 500)
    frame_label2  = show_label(frame2, "Right Frame", 12)
    frame_label2.config(relief=SUNKEN,background='light salmon', padding=(20,5))

    pane.add(frame1, weight=2)
    pane.add(frame2, weight=4)

    root.mainloop()


if __name__ == "__main__":
    main()
