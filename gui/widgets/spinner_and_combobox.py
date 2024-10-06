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
# Description : demonstrate the use of combobox      #
#               & spinner.                            #
# -------------------------------------------------- #

from tkinter import *
from tkinter import ttk
import calendar
from gui.utils import show_label

def show_spinner(val,label):
    print(val.get())
    label.config(text = "Spinner",background="gray", padding=5)


def show_combobox(val,label):
    print(val.get())
    label.config(text = "Checkbox",background="yellow", padding=5)


def main():
    root = Tk()
    # setting theme of GUI
    style = ttk.Style(root)
    style.theme_use('vista')

    title = show_label(root, "ComboBox and Spinner", 16)
    title.config(background="#a48923")
    label = show_label(root, "Item Selected:", 10)

    # combobox
    month_list = list(calendar.month_name)[1:]
    month = StringVar()
    combobox = ttk.Combobox(root, textvariable=month)
    combobox.pack()
    combobox.config(values= month_list, postcommand= lambda : show_combobox(month,label))
    combobox.set(month_list[5])

    #spiner
    date = StringVar()
    spinner_date = ttk.Spinbox(root, textvariable=date)
    spinner_date.pack()
    spinner_date.config(from_= 1, to=31, command= lambda : show_spinner(date,label))
    spinner_date.set(5)

    root.mainloop()


if __name__ == "__main__":
    main()
