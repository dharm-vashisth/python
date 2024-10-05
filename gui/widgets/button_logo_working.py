# @author: Dharm Vashisth
# @date: 2024-10-05
from tkinter import *
from tkinter import ttk


def get_logo():
    return PhotoImage(file="..\\..\\images\\robo.png")


def call_me(btn_text):
    print(f"Button with text as {btn_text} is Clicked!")


def main():
    root = Tk()

    # button with image and text
    text_btn_1 = "Click me"
    # use lambda function to pass argument to the command method.
    my_button = ttk.Button(root, text=text_btn_1, command=lambda: call_me(text_btn_1))
    my_button.pack()
    logo = get_logo()
    my_button.config(image=logo, compound=LEFT)

    # button 2 with small image
    text_btn_2 = "Click small button"
    logo2 = (logo.subsample(2, 2))
    my_button2 = ttk.Button(root, text=text_btn_2, command=lambda: call_me(text_btn_2))
    my_button2.pack()
    my_button2.config(image=logo2, compound=RIGHT)

    root.mainloop()


if __name__ == "__main__":
    main()
