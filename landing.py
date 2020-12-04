from tkinter import *
import pyglet
from PIL import ImageTk,Image

# Adding Custom Font
pyglet.font.add_file('./Assets/Product Sans Regular.ttf')


#root layout
root = Tk()
root.geometry('700x500')

# image as a bg
load = Image.open('./Assets/landing.png')
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0, y=0)

# Add Bus Window
def AddBus():
    add_bus_app = Tk()
    add_bus_app.geometry('700x500')
    labelExample = Label(add_bus_app, text = "New Window").pack()
    
        
# Search Bus Window
def SearchBus():
    search_bus_app = Tk()
    search_bus_app.geometry('700x500')
    labelExample = Label(search_bus_app, text = "New Window").pack()    

# Buttons
label_add = Label(root, text='(For Operators)', font=('Product Sans Regular', 15), bg="#ffd5bc")
label_add.place(x=45, y=370)
label_search = Label(root, text='(For Customers)', font=('Product Sans Regular', 15), bg="#ffd5bc")
label_search.place(x=510, y=370)
add_bus_img = PhotoImage(file = './Assets/add_bus.png')
add_bus = Button(root, image=add_bus_img, bd=0, bg="#ffd5bc", activebackground="#ffd5bc",command=AddBus)
add_bus.place(x=20, y=400)

search_bus_img = PhotoImage(file = './Assets/search_bus.png')
search_bus = Button(root, image=search_bus_img, bd=0, bg="#ffd5bc", activebackground="#ffd5bc", command=SearchBus)
search_bus.place(x=470, y=400)

root.mainloop()
