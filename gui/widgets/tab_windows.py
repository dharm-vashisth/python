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
# Description : [Description]                        #
#                                                    #
# -------------------------------------------------- #

from tkinter import *
from tkinter import ttk

from gui.login_form import show_login_form
from gui.utils import (
    show_label,
    show_frame,
)


def main():
    root = Tk()

    title = show_label(root, "CyberHub", 16)
    label = show_label(root, "Tab separated windows:", 10)
    notebook = ttk.Notebook(root)
    notebook.pack()

    frame1 = show_login_form(notebook)
    frame2 = show_frame(notebook, width=200, height=400)
    frame2_label = show_label(frame2, "We are Awesome", 12)
    frame2_label.config(padding=(20,5), background='olive')

    frame2_label2 = show_label(frame2, "You are one of us", 12)
    frame2_label2.config(padding=(20,5), background='magenta')

    notebook.add(frame1,text="Login")
    notebook.add(frame2, text="About Us")
    root.mainloop()


if __name__ == "__main__":
    main()
