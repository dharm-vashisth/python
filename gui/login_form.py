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
from tkinter import (
    ttk,
    messagebox,
)

from gui.utils import (
    show_label,
    show_entry_field,
)


def clear_things(user,password):
    user_name_value = user.get()
    user_pass_value = password.get()
    if user_name_value.strip() != '' and user_pass_value.strip()!='':
        messagebox.showinfo("Information","Form Submitted")
        user.set('')
        password.set('')
    else:
        messagebox.showwarning("Warning", "All form fields are mandatory")
    # print(f"User: {user_name_value} and Password: {user_pass_value}")

def show_login_form(master):
    frame = ttk.Frame(master,width=400, height=200)
    frame.pack()
    frame.config(relief= RIDGE, padding=(20,10))

    # variables to store value
    user_name = StringVar()
    user_pass = StringVar()

    label = show_label(frame, "Login Form", 10)

    label_name = show_label(frame, "User Name:", 8)
    user_name_entry = show_entry_field(frame, user_name)

    label_pass = show_label(frame, "Password: ", 8)
    user_pass_entry = show_entry_field(frame, user_pass)
    user_pass_entry.config(show='*')

    submit_button = ttk.Button(frame, text="Submit", padding=(5,2))
    submit_button.pack()
    submit_button.config(command= lambda: clear_things(user_name,user_pass))

    return frame

def main():
    root = Tk()
    root.geometry('500x600')

    title = show_label(root, "CyberHub", 16)
    title.config(background='olive', foreground='white')
    frame = show_login_form(root)
    root.mainloop()


if __name__ == "__main__":
    main()
