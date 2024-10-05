from tkinter import *
from tkinter import ttk
root = Tk() # top level window
button = ttk.Button(root,text = "Click Me") # theme button is created
button.pack() # attach the button on the root window
print(button['text'])
button.config(text = 'Push Me') # changing text of button way 1
print(button['text'])
print(button.config())
button['text'] = "I'm button"  # changing text of button way 2
root.mainloop()
