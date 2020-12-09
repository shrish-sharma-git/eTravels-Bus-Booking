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
pyglet.font.add_file('./Assets/PSBold.ttf')

#root layout
root = Tk()
root.title('Welcome to eTravels - Book Bus Tickets')
root.geometry("700x500+120+120")

# this removes the maximize button
root.resizable(0,0)

# image as a background for root
load = Image.open('./Assets/landing.png')
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0, y=0)

#********************* ADD BUS WINDOW **********************
# Add Bus Window
def AddBus():
    add_bus_app = Toplevel()
    add_bus_app.geometry('700x500+120+120')

    # image as a background for Add Bus
    load_add_bg = Image.open('./Assets/add_bus_bg.png')
    render_add_bus = ImageTk.PhotoImage(load_add_bg)
    img_add_bus = Label(add_bus_app, image=render_add_bus)
    img_add_bus.image = render_add_bus
    img_add_bus.place(x=0, y=0)

    labelExample = Label(add_bus_app, text = "Welcome Operator!", font=('PSBold', 18), bg='#D1456E', fg='#fff').grid(row=0, column=1, columnspan=10, pady=10)

    home_button = Button(add_bus_app, image=home_btn, command=add_bus_app.destroy, bd=0, bg="#D1456E")
    home_button.place(x=10, y=10)

    # Header
    head_label = Label(add_bus_app, text="Add Details of Buses", font=('PSBold', 9), bg='#D1456E', fg='#fff').grid(row=1, column=1, pady=10, columnspan=10)

    #Getting Inputs    
    Agency_name = Entry(add_bus_app, width=60)
    Agency_name.grid(row=2, column=1, padx=20)

    Contact_Number = Entry(add_bus_app, width=60)
    Contact_Number.grid(row=3, column=1)

    Address = Entry(add_bus_app, width=60)
    Address.grid(row=4, column=1)

    Operator_Id = Entry(add_bus_app, width=60)
    Operator_Id.grid(row=5, column=1)

    Bus_Type = Entry(add_bus_app, width=60)
    Bus_Type.grid(row=6, column=1)

    loc_From = Entry(add_bus_app, width=60)
    loc_From.grid(row=7, column=1)

    loc_To = Entry(add_bus_app, width=60)
    loc_To.grid(row=8, column=1)

    Dep_Time = Entry(add_bus_app, width=60)
    Dep_Time.grid(row=9, column=1)

    Arrival_Time = Entry(add_bus_app, width=60)
    Arrival_Time.grid(row=10, column=1)

    Fare = Entry(add_bus_app, width=60)
    Fare.grid(row=11, column=1)

    Seats = Entry(add_bus_app, width=60)
    Seats.grid(row=12, column=1)

    # Adding Entry Labels
    Agency_name_label = Label(add_bus_app, text="Agency Name", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
    Agency_name_label.grid(row=2, column=0, padx=50)

    Contact_Number_label = Label(add_bus_app, text="Contact Number", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
    Contact_Number_label.grid(row=3, column=0)

    Address_label = Label(add_bus_app, text="Address", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
    Address_label.grid(row=4, column=0)

    Operator_Id_label = Label(add_bus_app, text="Operator Id", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
    Operator_Id_label.grid(row=5, column=0)

    Bus_Type_label = Label(add_bus_app, text="Bus Type", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
    Bus_Type_label.grid(row=6, column=0)

    loc_From_label = Label(add_bus_app, text="From Location", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
    loc_From_label.grid(row=7, column=0)

    loc_To_label = Label(add_bus_app, text="To Loaction", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
    loc_To_label.grid(row=8, column=0)

    Dep_Time_label = Label(add_bus_app, text="Departure Time", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
    Dep_Time_label.grid(row=9, column=0)

    Arrival_Time_label = Label(add_bus_app, text="Arrival TIme", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
    Arrival_Time_label.grid(row=10, column=0)

    Fare_label = Label(add_bus_app, text="$ Fare", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
    Fare_label.grid(row=11, column=0)

    Seats_label = Label(add_bus_app, text="Total Seats", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
    Seats_label.grid(row=12, column=0)

    # Submit Function for Database
    def submit():
        # Creating Database
        conn = sqlite3.connect('bus_list.db')

        # Create Cursor
        c = conn.cursor()

        # Insert DATA into Table
        c.execute("insert into BusList values(:Agency_name, :Contact_Number, :Address, :Operator_Id, :Bus_Type, :loc_From, :loc_To, :Dep_Time, :Arrival_Time, :Fare, :Seats)",
                  {
                      'Agency_name': Agency_name.get(),
                      'Contact_Number': Contact_Number.get(),
                      'Address': Address.get(),
                      'Operator_Id': Operator_Id.get(),
                      'Bus_Type': Bus_Type.get(),
                      'loc_From': loc_From.get(),
                      'loc_To': loc_To.get(),
                      'Dep_Time': Dep_Time.get(),
                      'Arrival_Time': Arrival_Time.get(),
                      'Fare': Fare.get(),
                      'Seats': Seats.get()
                      })

        # Commit Changes
        conn.commit()

        # Closing Connection
        conn.close()

        # Clear input after Submitting
        Agency_name.delete(0, END)
        Contact_Number.delete(0, END)
        Address.delete(0, END)
        Operator_Id.delete(0, END)
        Bus_Type.delete(0, END)
        loc_From.delete(0, END)
        loc_To.delete(0, END)
        Dep_Time.delete(0, END)
        Arrival_Time.delete(0, END)
        Fare.delete(0, END)
        Seats.delete(0, END)

    # Add Record to Database Button
    submit_btn = Button(add_bus_app, image=add_btn, bd=0, bg='#D1456E', command=submit).place(x=300, y=350)
    
    #add_bus_btn = Button(add_bus_app, text="Add Bus", command=submit)
    #add_bus_btn.grid(row=14, column=1, pady=50)
    

#********************* ADD BUS WINDOW ENDS******************************************************


#********************* SEARCH BUS WINDOW ***************************************************    
# Search Bus Window
def SearchBus():
    search_bus_app = Toplevel()
    search_bus_app.geometry('700x500+120+120')

    # image as a background for Add Bus
    load_src_bg = Image.open('./Assets/search_bus_bg.png')
    render_src_bus = ImageTk.PhotoImage(load_src_bg)
    img_src_bus = Label(search_bus_app, image=render_src_bus)
    img_src_bus.image = render_src_bus
    img_src_bus.place(x=0, y=0)

    labelExample = Label(search_bus_app, text = "Welcome Customer!", font=('PSBold', 18), bg='#D1456E', fg='#fff').grid(row=0, column=1, pady=10)
    #home_btn = Button(search_bus_app, text="Home", command=search_bus_app.destroy).grid(row=1, column=1)

    # Header
    head_label = Label(search_bus_app, text="Search Your Bus!", font=('PSBold', 9), bg='#D1456E', fg='#fff').grid(row=2, column=1)

    # Bus Type DropDown
    click = StringVar()
    click.set("Choose Your Bus Type")
    bus_type_dropd = OptionMenu(search_bus_app, click, "AC", "Non-AC", "AC-Sleeper", "Non-AC-Sleeper", "All Types")
    bus_type_dropd.config(width = 40)
    bus_type_dropd.grid(row=3, column=1, pady=30)

    # Labels
    loc_From_label = Label(search_bus_app, text="From Location", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
    loc_From_label.grid(row=5, column=0, padx=50)

    loc_To_label = Label(search_bus_app, text="To Loaction", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
    loc_To_label.grid(row=6, column=0, padx=10)

    # Entries
    loc_From = Entry(search_bus_app, width=60)
    loc_From.grid(row=5, column=1)

    loc_To = Entry(search_bus_app, width=60)
    loc_To.grid(row=6, column=1)

    #Search Function Beta
    def Search():
        search_app = Toplevel()
        search_app.geometry('700x500+120+120')

        # Getting Entry Values and keeping them here
        drop_val = click.get()
        loc_from_val = loc_From.get()
        loc_to_val = loc_To.get()
        
        # Creating Database
        conn = sqlite3.connect('bus_list.db')

        # Create Cursor
        c = conn.cursor()

        # Querying the Database
        c.execute("Select * from BusList")
        rec = c.fetchall()
        for r in rec:
            Label(search_app, text=str(r)).pack()

        # Commit Changes
        conn.commit()

        # Closing Connection
        conn.close()


    # Search Button
    search_btn = Button(search_bus_app, image=src_btn, bd=0, bg='#D1456E', command=Search).place(x=270, y=240)    

#********************* SEARCH BUS WINDOW ENDS************************************************************    
    

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

# Add Bus App Button Image (Global)
add_btn = ImageTk.PhotoImage(Image.open("./Assets/add_bus_child.png"))

# Search Bus App Button Image (Global)
src_btn = ImageTk.PhotoImage(Image.open("./Assets/search_bus_child.png"))

# Hime Button (Global)
home_btn = ImageTk.PhotoImage(Image.open("./Assets/home.png"))

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
