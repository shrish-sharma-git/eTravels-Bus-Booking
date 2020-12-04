from tkinter import *
from PIL import ImageTk,Image

#root layout
root = Tk()
root.geometry('700x500')

# image as a bg
load = Image.open('./Assets/landing.png')
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0, y=0)


# Buttons
add_bus = Button(root, text="Add Bus").pack()
search_bus = Button(root, text="Search Bus").pack()


root.mainloop()
