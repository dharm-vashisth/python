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
# Description : Text Enrty                           #
#                                                    #
# -------------------------------------------------- #
from tkinter import *
from tkinter import (
    ttk,
    messagebox,
)

from gui.utils import show_label


def print_text_value(textbox):
    content = (f"first line: {textbox.get('1.0', '1.0 lineend')} \nSecond Line: {textbox.get('2.0', '2.0 lineend')}."+
               f"\nFull Content:\n{textbox.get('1.0', END)}")
    messagebox.showinfo("Content", content)  # full content.


def main():
    root = Tk()

    title = show_label(root, "Multiline text box", 16)
    label = show_label(root, "Provide multiline entry:", 10)
    text_entry = Text(root, width=40, height=10)
    text_entry.pack()

    submit_button = ttk.Button(root, text="Submit Text")
    submit_button.pack()
    submit_button.config(command=lambda: print_text_value(text_entry))

    root.mainloop()


if __name__ == "__main__":
    main()
