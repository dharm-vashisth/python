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
# Description : window implementation                #
#                                                    #
# -------------------------------------------------- #

from tkinter import *
from tkinter import ttk

from gui.utils import show_label

class SideWindow:
    window = None

    def child_window(self,root):
        self.window = Toplevel(root)
        self.window.title("Child Window")
        self.window.geometry('100x200+10+20')

        button = ttk.Button(self.window, text="Minimize Window")
        button.pack()
        button.config(command=self.minimize)

        button2 = ttk.Button(self.window, text="Close Window")
        button2.pack()
        button2.config(command=self.destroy_window)

    def minimize(self):
        self.window.iconify()

    def destroy_window(self):
        return self.window.destroy()

def main():
    root = Tk()
    side_window = SideWindow()
    title = show_label(root, "Nested Window", 16)
    label = show_label(root, "Child Window:", 10)

    button = ttk.Button(root,text = "Create Window")
    button.pack()
    button.config(command= lambda: side_window.child_window(root))

    root.mainloop()


if __name__ == "__main__":
    main()
