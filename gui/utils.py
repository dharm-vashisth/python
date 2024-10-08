from tkinter import *
from tkinter import ttk


def show_label(master, text_msg, font_size=16):
    my_label = ttk.Label(master, text=text_msg)
    my_label.pack()
    my_label.config(wraplength=350, font=('Arial', font_size, 'bold'), justify=CENTER)
    return my_label

def show_entry_field(master,var):
    user_name_entry = ttk.Entry(master, textvariable=var)
    user_name_entry.pack()
    return user_name_entry

def show_frame(master, width, height):
    frame = ttk.Frame(master, width= width, height=height)
    frame.pack()
    frame.config(relief= SUNKEN)
    return frame
