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
add_bus_img = PhotoImage(file = './Assets/add_bus.png')
add_bus = Button(root, image=add_bus_img, bd=0, bg="#ffd5bc", activebackground="#ffd5bc")
add_bus.place(x=20, y=400)

search_bus_img = PhotoImage(file = './Assets/search_bus.png')
search_bus = Button(root, image=search_bus_img, bd=0, bg="#ffd5bc", activebackground="#ffd5bc")
search_bus.place(x=470, y=400)

root.mainloop()
