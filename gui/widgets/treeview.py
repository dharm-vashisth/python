# -------------------------------------------------- #
#  ____    __      __                                #
# |  _ \   \ \    / /                                #
# | | | |   \ \  / /                                 #
# | | | |    \ \/ /                                  #
# | |_| |     \  /                                   #
# |____/       \/                                    #
# -------------------------------------------------- #
# Author      : Dharm Vashisth                       #
# Created on  : 2024-10-12                           #
# Description : Tree View                            #
#                                                    #
# -------------------------------------------------- #

from tkinter import *
from tkinter import ttk
from gui.utils import show_label

def toggle(treeview, button):
    if button['text'] == 'Attach':
        button['text']='De-attach'
        treeview.move('item3','','end')
    else:
        treeview.detach('item3')
        button['text'] = 'Attach'

def main():
    root = Tk()

    title = show_label(root, "Tree View", 16)
    treeview = ttk.Treeview(root)
    treeview.pack()
    treeview.insert('',0,'item1',text= 'First item') # at parent level
    treeview.insert('',1,'item2',text= 'Second item') # at parent level
    treeview.insert('','end','item3',text= 'Third item') # at parent level

    label = show_label(root, "Tree view with hierarchy", 10)

    # de-attach item with the click of a button
    button = ttk.Button(root, text = 'De-attach')
    button.pack()
    button.config(command= lambda : toggle(treeview,button))

    image = PhotoImage(file = '..//..//images//robo.png').subsample(10,10)

    # adding child to item1
    treeview.insert('item1',0,'item1.1',text= "Child 1")
    treeview.insert('item1', 'end', 'item1.2', text="Image 1", image=image)
    treeview.insert('item1', 2, 'item1.3', text="Child 3")
    # property of item: open
    treeview.item('item1', open=True) # items will be expanded.

    # adding child to item1
    treeview.insert('item2',0,'item2.1',text= "Child 1")
    treeview.insert('item2', 2, 'item2.3', text="Child 3")
    treeview.insert('item2', 'end', 'item2.2', text="Image 2", image=image)

    # now images parent will be changed to item 3.
    treeview.move('item2.2','item3',1)
    treeview.move('item1.2', 'item3', 2)

    root.mainloop()


if __name__ == "__main__":
    main()
