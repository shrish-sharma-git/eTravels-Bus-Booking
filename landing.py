# Tkinter Library
from tkinter import *

# Custom Font Library
import pyglet

# SQLite Library
import sqlite3

# Pillow Library for Images
from PIL import ImageTk,Image

# Adding Custom Font
pyglet.font.add_file('./Assets/Product Sans Regular.ttf')

#root layout
root = Tk()
root.title('Welcome to eTravels - Book Bus Tickets')
root.geometry("700x500+120+120")

# image as a bg
load = Image.open('./Assets/landing.png')
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0, y=0)

# Add Bus Window
def AddBus():
    add_bus_app = Tk()
    add_bus_app.geometry('700x500+120+120')
    labelExample = Label(add_bus_app, text = "Welcome Operator!").pack()
    home_btn = Button(add_bus_app, text="Home", command=add_bus_app.destroy).pack()
    
        
# Search Bus Window
def SearchBus():
    search_bus_app = Tk()
    search_bus_app.geometry('700x500+120+120')
    labelExample = Label(search_bus_app, text = "Welcome Customer!").pack()
    home_btn = Button(search_bus_app, text="Home", command=search_bus_app.destroy).pack()    

# Buttons
label_add = Label(root, text='(For Operators)', font=('Product Sans Regular', 15), bg="#ffd5bc")
label_add.place(x=35, y=370)
label_search = Label(root, text='(For Customers)', font=('Product Sans Regular', 15), bg="#ffd5bc")
label_search.place(x=510, y=370)
add_bus_img = PhotoImage(file = './Assets/add_bus.png')
add_bus = Button(root, image=add_bus_img, bd=0, bg="#ffd5bc", activebackground="#ffd5bc",command=AddBus)
add_bus.place(x=20, y=400)

search_bus_img = PhotoImage(file = './Assets/search_bus.png')
search_bus = Button(root, image=search_bus_img, bd=0, bg="#ffd5bc", activebackground="#ffd5bc", command=SearchBus)
search_bus.place(x=470, y=400)

#********************************************** DATABASE *************************************************#

# Creating Database
conn = sqlite3.connect('bus_list.db')

# Create Cursor
c = conn.cursor()

# Creating Table
c.execute("""CREATE TABLE if not exists BusList(Agency_Name varchar(30) not null, Contact_Number int(10) not null, Address varchar(30) not null, Operator_Id int(10) not null, Bus_Type varchar(15) not null, loc_From varchar(50) not null, loc_To varchar(50) not null, Departure_Time varchar(10) not null, Arrival_Time varchar(10) not null, fare int(10), num_seats int(50) not null, primary key(Operator_Id))""")

# Commit Changes
conn.commit()

# Closing Connection
conn.close()

#********************************************** DATABASE *************************************************#
root.mainloop()
