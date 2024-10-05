# @author: Dharm Vashisth
# @date: 2024-10-05
from tkinter import *
from tkinter import ttk
from gui.utils import show_label


def show_checkbox_value(value):
    print(value.get())


def main():
    root = Tk()

    title = show_label(root, "Radio",16)
    label = show_label(root, "Select the diet type:",10)

    # bind variable to radio
    radio_value = StringVar()

    # radio 1
    text_rad_1 = "Veg"
    veg = ttk.Radiobutton(root, text=text_rad_1)
    veg.pack()
    veg.config(variable=radio_value, value=text_rad_1,
                 command=lambda: show_checkbox_value(radio_value))

    # radio 2
    text_rad_2 = "Vegan"
    vegan = ttk.Radiobutton(root, text=text_rad_2)
    vegan.pack()
    vegan.config(variable=radio_value, value=text_rad_2,
                 command=lambda: show_checkbox_value(radio_value))


    root.mainloop()


if __name__ == "__main__":
    main()
