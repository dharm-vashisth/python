# -------------------------------------------------- #
#  ____    __      __                                #
# |  _ \   \ \    / /                                #
# | | | |   \ \  / /                                 #
# | | | |    \ \/ /                                  #
# | |_| |     \  /                                   #
# |____/       \/                                    #
# -------------------------------------------------- #
# Author      : Dharm Vashisth                       #
# Created on  : 2024-10-06                           #
# Version     : v1.0                                 #
# Description : Convert text to sound.               #
#                                                    #
# -------------------------------------------------- #

import os
from tkinter import *
from tkinter import ttk

from gtts import gTTS

def show_label(master, text_msg, font_size=16):
    my_label = ttk.Label(master, text=text_msg)
    my_label.pack()
    my_label.config(wraplength=350, font=('Arial', font_size, 'bold'), justify=CENTER)
    return my_label

def text_to_voice(text, directory, filename):
    # Ensure the directory exists
    text_message = text.get()
    directory_value = directory.get()
    file_name = filename.get()

    if not os.path.exists(directory_value):
        os.makedirs(directory_value)

    # Create the full path for the output file
    file_path = os.path.join(directory_value, f"{file_name}.mp3")

    # Convert the text to speech
    tts = gTTS(text=text_message, lang='en')

    # Save the audio file
    tts.save(file_path)
    print(f"Audio saved at: {file_path}")

def main():
    root = Tk()
    root.title("Text to voice")
    root.config(borderwidth=2, padx=5, pady=5, background='#ffa0f4')
    style = ttk.Style(root)
    style.theme_use('alt')

    title = show_label(root, "Text translator", 16)
    title.config(background="yellow", padding=5)

    label = show_label(root, "Enter the text message:", 10)
    label.config(background="blue", foreground="white")

    text_message = StringVar()
    entry = ttk.Entry(root,"", textvariable = text_message)
    entry.pack()

    label = show_label(root, "Enter the directory name:", 10)
    label.config(background="blue", foreground="white")

    directory_name = StringVar()
    entry = ttk.Entry(root, "", textvariable=directory_name)
    entry.pack()

    label = show_label(root, "Enter the file name:", 10)
    label.config(background="blue", foreground="white")

    file_name = StringVar()
    entry = ttk.Entry(root, "", textvariable=file_name)
    entry.pack()

    submit_button = ttk.Button(root,text="Convert")
    submit_button.pack()
    submit_button.config(padding=2,command=lambda: text_to_voice(text_message, directory_name,file_name))

    root.mainloop()

if __name__ == "__main__":
    main()
