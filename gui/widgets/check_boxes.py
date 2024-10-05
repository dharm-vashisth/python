# @author: Dharm Vashisth
# @date: 2024-10-05
from tkinter import *
from tkinter import ttk
from gui.utils import show_label


def show_checkbox_value(value):
    print(value.get())


def main():
    root = Tk()

    label = show_label(root, "Select the pizza toppings:",12)

    # checkbox
    text_chk_1 = "Tomato"
    tomato_chk = ttk.Checkbutton(root, text=text_chk_1)
    tomato_chk.pack()
    # bind variable with checkbox
    tomato_value = StringVar()
    tomato_chk.config(variable=tomato_value, onvalue="Tomato is selected", offvalue="Tomato is not selected",
                 command=lambda: show_checkbox_value(tomato_value))

    # checkbox2
    text_chk_2 = "Onion"
    onion_chk = ttk.Checkbutton(root, text=text_chk_2)
    onion_chk.pack()
    # bind variable with checkbox
    onion_value = StringVar()
    onion_chk.config(variable=onion_value, onvalue="Onion is selected", offvalue="Onion is not selected",
                 command=lambda: show_checkbox_value(onion_value))

    # checkbox3
    text_chk_3 = "Cheese"
    cheese_chk = ttk.Checkbutton(root, text=text_chk_3)
    cheese_chk.pack()
    # bind variable with checkbox
    cheese_value = StringVar()
    cheese_chk.config(variable=cheese_value, onvalue="Cheese is selected", offvalue="Cheese is not selected",
                 command=lambda: show_checkbox_value(cheese_value))

    root.mainloop()


if __name__ == "__main__":
    main()
