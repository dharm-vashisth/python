# @author: Dharm Vashisth
# @date: 2024-10-05

from tkinter import *
from tkinter import ttk


class Hello:
    def __init__(self, master):
        self.label = ttk.Label(master, text="Hello Tkinter!")
        self.label.pack()
        # adding buttons to root
        ttk.Button(master, text="Client", command=self.hello_client).pack()
        ttk.Button(master, text="User", command=self.hello_user).pack()

    def hello_client(self):
        self.label.config(text="Hello Client")

    def hello_user(self):
        self.label.config(text="Hello User")


def main():
    root = Tk()
    root.title("Interative Hello")
    app = Hello(root)
    root.mainloop()


if __name__ == '__main__':
    main()
