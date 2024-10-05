from tkinter import *
from gui.utils import show_label

root = Tk()
label = show_label(root, "Welcome to the GUI version of Python")

# image used in logo as two level up
logo = PhotoImage(file="../../images/robo.png")

# properties of label
label.config(wraplength=350, foreground="navy", background="gray", font=('Arial', 16, 'bold'), justify=CENTER)
label.config(image=logo)  # setting logo to use image instead of text
label.config(compound=LEFT)  # display both text and image with position as left

root.mainloop()
