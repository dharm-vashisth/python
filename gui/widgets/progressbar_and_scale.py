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
# Description : Progressbar and scale                #
#                                                    #
# -------------------------------------------------- #

from tkinter import *
from tkinter import ttk
from gui.utils import show_label


def check_progress_2(e,progress, progressbar2):
    d= progress.get()
    if d == 100:
        progressbar2.stop()
    else:
        progressbar2.start()


def main():
    root = Tk()

    title = show_label(root, "Progressbar and Scale", 16)
    max_value = 100.0
    dummy_value = 23.0
    progress = DoubleVar()

    label = show_label(root, "Progress Bar: determinate", 10)

    progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=150)
    progressbar.pack()
    progressbar.config(mode='determinate', maximum=max_value, value=dummy_value, variable=progress)
    label = show_label(root, "Progress Bar: indeterminate", 10)

    progressbar2 = ttk.Progressbar(root, orient=HORIZONTAL, length=150)
    progressbar2.pack()
    progressbar2.config(mode='indeterminate', maximum=max_value)

    label = show_label(root, "Scale: drag scale to start indeterminate progressbar", 10)
    scale = ttk.Scale(root, orient=HORIZONTAL)
    scale.pack()
    scale.config(from_=1, to=max_value, value=dummy_value, variable=progress,
                 command= lambda a: check_progress_2(a,progress, progressbar2))

    root.mainloop()


if __name__ == "__main__":
    main()
