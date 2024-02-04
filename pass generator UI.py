import random
import string
import tkinter as tk
from tkinter import *

win = Tk()
win.geometry('309x150')
win.title("Password Generator")
win.resizable(False, False)
win.configure(bg="#39C293")

def generate(text_widget, length=11):
    # Define characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))

    # Delete any existing text in the Text widget
    text_widget.delete(1.0, END)

    # Calculate the center position
    center_position = max(0, (14 - len(password)) // 2)

    # Insert the generated password at the center of the Text widget
    text_widget.insert(1.0, ' ' * center_position + password)

    # Append the generated password to the file
    with open('../password.txt', 'a') as file:
        file.write(password + '\n')

    # Return the generated password
    return password

def copy_to_clipboard(text_widget):
    password = text_widget.get("1.0", "end-1c")
    if password:
        win.clipboard_clear()
        win.clipboard_append(password)
        win.update()

        # Optionally, you can provide user feedback
        text_widget.delete(1.0, END)
        text_widget.insert(1.0, "Copied!")

Text4Result = Text(win, width=12, height=1, bg="#ffffff", font=('Google Sans', 15), wrap=NONE)
Text4Result.place(x=90, y=60)

Button(win, text="Generate", width=7, height=1, bg="white", fg="black", bd=3, highlightbackground="black", font=("Google Sans", 11, ),
       command=lambda: generate(Text4Result)).place(x=10, y=60)

Button(win, text="Copy", width=7, height=1, bg="white", fg="black", bd=3, highlightbackground="black", font=("Google Sans", 11, ),
       command=lambda: copy_to_clipboard(Text4Result)).place(x=10, y=95)

win.mainloop()
