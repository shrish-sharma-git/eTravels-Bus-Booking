# Tkinter Library
from tkinter import *
from tkinter import messagebox

# Custom Font Library
import pyglet

# SQLite Library
import sqlite3

# Pillow Library for Images
from PIL import ImageTk,Image

# Adding Custom Font
pyglet.font.add_file('./Assets/Product Sans Regular.ttf')
pyglet.font.add_file('./Assets/PSBold.ttf')

#************** SPLASH SCREEN**************#
# Splash Screen
s_root = Tk()
s_root.geometry('800x700+300+50')
s_root.overrideredirect(True)

# Setting Splash Screen
load_splash_bg = Image.open('./Assets/splash_screen.png')
render_splash = ImageTk.PhotoImage(load_splash_bg)
img_splash = Label(s_root, image=render_splash)
img_splash.image = render_splash
img_splash.place(x=0, y=0)

s_root.after(5000, s_root.destroy)
s_root.mainloop()

#************** SPLASH SCREEN**************#

#root layout
root = Tk()
root.title('Welcome to eTravels - Book Bus Tickets')
root.geometry("800x700+300+50")
root.iconbitmap('./Assets/root_icon.ico')

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
    add_bus_app.geometry('800x700+300+50')
    add_bus_app.iconphoto(False, icon_photo)

    # image as a background for Add Bus
    load_add_bg = Image.open('./Assets/add_bus_bg.png')
    render_add_bus = ImageTk.PhotoImage(load_add_bg)
    img_add_bus = Label(add_bus_app, image=render_add_bus)
    img_add_bus.image = render_add_bus
    img_add_bus.place(x=0, y=0)

    labelExample = Label(add_bus_app, text = "Welcome Operator!", font=('PSBold', 18), bg='#D1456E', fg='#fff').grid(row=0, column=1, columnspan=10, pady=5)

    # Home Button
    # Home Button Function
    def home_fun():
        response = messagebox.askyesno("Go to Homepage?", "Are You Sure?", parent=add_bus_app)
        if response == True:
            add_bus_app.destroy()
            
    home_button = Button(add_bus_app, image=home_btn, command=home_fun, bd=0, bg="#D1456E")
    home_button.place(x=10, y=10)

    # Header
    head_label = Label(add_bus_app, text="Add Details of Buses", font=('PSBold', 9), bg='#D1456E', fg='#fff').grid(row=1, column=1, pady=10, columnspan=10)

    #Getting Inputs
    #Defining String Variables for each entry
    Full_name = StringVar()
    Contact_no = StringVar()
    Address = StringVar()
    Agency_name = StringVar()
    Bus_type = StringVar()
    loc_From = StringVar()
    loc_To = StringVar()
    Date = StringVar()
    Dep_Time = StringVar()
    Arrival_Time = StringVar()
    fare = StringVar()
    seats = StringVar()

    # Entry Inputs
    txtFull_name = Entry(add_bus_app, width=60, textvariable=Full_name)
    txtFull_name.grid(row=2, column=1, padx=20, pady=5)

    txtContact_Number = Entry(add_bus_app, width=60, textvariable=Contact_no)
    txtContact_Number.grid(row=3, column=1, pady=5)

    txtAddress = Entry(add_bus_app, width=60, textvariable=Address)
    txtAddress.grid(row=4, column=1, pady=5)

    
    # Adding Entry Labels
    Full_name_label = Label(add_bus_app, text="Full Name", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
    Full_name_label.grid(row=2, column=0, padx=50)

    Contact_Number_label = Label(add_bus_app, text="Contact Number", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
    Contact_Number_label.grid(row=3, column=0)

    Address_label = Label(add_bus_app, text="Address", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
    Address_label.grid(row=4, column=0)


    # Submit Function for Database
    def Main_Details():
        # calling fun to add data in operator
        if(len(Full_name.get())!=0):
            Add_Operator_Record(Full_name.get(), Contact_no.get(), Address.get())
        else:
            messagebox.showerror("Error!", "Please Make Sure to Fill all the Input Fields!")
    
        # Entries
        txtAgency_Name = Entry(add_bus_app, width=60, textvariable=Agency_name)
        txtAgency_Name.grid(row=6, column=1, pady=5)

        txtBus_Type = Entry(add_bus_app, width=60, textvariable=Bus_type)
        txtBus_Type.grid(row=7, column=1, pady=5)

        txtloc_From = Entry(add_bus_app, width=60, textvariable=loc_From)
        txtloc_From.grid(row=8, column=1, pady=5)

        txtloc_To = Entry(add_bus_app, width=60, textvariable=loc_To)
        txtloc_To.grid(row=9, column=1, pady=5)

        txtdate = Entry(add_bus_app, width=60, textvariable=Date)
        txtdate.grid(row=10, column=1, pady=5)
        
        txtDep_Time = Entry(add_bus_app, width=60, textvariable=Dep_Time)
        txtDep_Time.grid(row=11, column=1, pady=5)

        txtArrival_Time = Entry(add_bus_app, width=60, textvariable=Arrival_Time)
        txtArrival_Time.grid(row=12, column=1, pady=5)

        txtFare = Entry(add_bus_app, width=60, textvariable=fare)
        txtFare.grid(row=13, column=1, pady=5)

        txtSeats = Entry(add_bus_app, width=60, textvariable=seats)
        txtSeats.grid(row=14, column=1, pady=5)

        # Labels
        Agency_name_label = Label(add_bus_app, text="Agency Name", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
        Agency_name_label.grid(row=6, column=0)

        Bus_Type_label = Label(add_bus_app, text="Bus Type", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
        Bus_Type_label.grid(row=7, column=0)

        loc_From_label = Label(add_bus_app, text="From Location", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
        loc_From_label.grid(row=8, column=0)

        loc_To_label = Label(add_bus_app, text="To Loaction", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
        loc_To_label.grid(row=9, column=0)

        date_label = Label(add_bus_app, text="Date", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
        date_label.grid(row=10, column=0)
        
        Dep_Time_label = Label(add_bus_app, text="Departure Time", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
        Dep_Time_label.grid(row=11, column=0)

        Arrival_Time_label = Label(add_bus_app, text="Arrival TIme", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
        Arrival_Time_label.grid(row=12, column=0)

        Fare_label = Label(add_bus_app, text="$ Fare", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
        Fare_label.grid(row=13, column=0)

        Seats_label = Label(add_bus_app, text="Total Seats", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
        Seats_label.grid(row=14, column=0)

        # The Add Bus Button (2nd on Add Bus Page)
        submit_btn = Button(add_bus_app, image=add_btn, bd=0, bg='#D1456E', command=Add_Record).grid(row=15, column=1)

    def Add_Record():
        if(len(Agency_name.get()) != 0):
            Add_Bus_Record(Agency_name.get(), Bus_type.get(), loc_From.get(), loc_To.get(), Date.get(), Dep_Time.get(), Arrival_Time.get(), fare.get(), seats.get())
            # Clear input after Submitting
            # Clear input after Submitting
            Full_name.set('')
            Contact_no.set('')
            Address.set('')
            
            Agency_name.set('')
            Bus_type.set('')
            loc_From.set('')
            loc_To.set('')
            Date.set('')
            Dep_Time.set('')
            Arrival_Time.set('')
            fare.set('')
            seats.set('')
            messagebox.showinfo("Success!", "Your Bus has been added and now is available for live bookings!")
        else:
            messagebox.showerror("Error!", "Please Make Sure to Fill all the Input Fields!")
          
    # The Add Details Button (1st on Add Bus Page)
    submit_btn = Button(add_bus_app, image=add_det_btn, bd=0, bg='#D1456E', command=Main_Details).grid(row=5, column=1)
    
#********************* ADD BUS WINDOW ENDS******************************************************


#********************* SEARCH BUS WINDOW ***************************************************    
# Search Bus Window
def SearchBus():
    search_bus_app = Toplevel()
    search_bus_app.geometry('800x700+300+50')
    search_bus_app.iconphoto(False, icon_photo)

    # image as a background for Add Bus
    load_src_bg = Image.open('./Assets/search_bus_bg.png')
    render_src_bus = ImageTk.PhotoImage(load_src_bg)
    img_src_bus = Label(search_bus_app, image=render_src_bus)
    img_src_bus.image = render_src_bus
    img_src_bus.place(x=0, y=0)

    labelExample = Label(search_bus_app, text = "Welcome Customer!", font=('PSBold', 18), bg='#D1456E', fg='#fff').grid(row=0, column=1, pady=10)

    # Home Button
    # Home Button Function
    def home_fun():
        response = messagebox.askyesno("Go to Homepage?", "Are You Sure?", parent=search_bus_app)
        if response == True:
            search_bus_app.destroy()
            
    
    home_button = Button(search_bus_app, image=home_btn, command=home_fun, bd=0, bg="#D1456E")
    home_button.place(x=10, y=10)
    
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

    date_label = Label(search_bus_app, text="Date", font=('Product Sans Regular', 10), fg='#fff', bg='#D1456E')
    date_label.grid(row=7, column=0, padx=10)    

    # Entries
    # String Vars
    loc_From = StringVar()
    loc_To = StringVar()
    date = StringVar()
    txtloc_From = Entry(search_bus_app, width=60, textvariable = loc_From)
    txtloc_From.grid(row=5, column=1)

    txtloc_To = Entry(search_bus_app, width=60, textvariable = loc_To)
    txtloc_To.grid(row=6, column=1)

    txtdate = Entry(search_bus_app, width=60, textvariable = date)
    txtdate.grid(row=7, column=1)

    #Search Function Beta
    def Search():
        search_app = Toplevel()
        search_app.geometry('800x700+300+50')
        # image as a background for Add Bus
        load_src_bg = Image.open('./Assets/results_bg.png')
        render_src_bus = ImageTk.PhotoImage(load_src_bg)
        img_src_bus = Label(search_app, image=render_src_bus)
        img_src_bus.image = render_src_bus
        img_src_bus.place(x=0, y=0)

        if(len(loc_From.get())!=0):
            #Printing the results on Search Screen
            #header
            #search_head = Label(search_app, text="Available Buses", font=("PSBold", 18)).pack()
            for row in Search_Bus(loc_From.get(), loc_To.get(), date.get()): 
                print(row)
                Label(search_app, text=str(row) + "\n").pack()
        else:
            messagebox.showerror("Error!", "Please Make Sure to Fill all the Input Fields!")
            
    # Search Button
    search_btn = Button(search_bus_app, image=src_btn, bd=0, bg='#D1456E', command=Search).place(x=270, y=240)    

#********************* SEARCH BUS WINDOW ENDS************************************************************    
    

# Buttons
label_add = Label(root, text='(For Operators)', font=('Product Sans Regular', 15), bg="#ffd5bc")
label_add.place(x=35, y=500)
label_search = Label(root, text='(For Customers)', font=('Product Sans Regular', 15), bg="#ffd5bc")
label_search.place(x=610, y=500)
add_bus_img = PhotoImage(file = './Assets/add_bus.png')
add_bus = Button(root, image=add_bus_img, bd=0, bg="#ffd5bc", activebackground="#ffd5bc",command=AddBus)
add_bus.place(x=20, y=540)

search_bus_img = PhotoImage(file = './Assets/search_bus.png')
search_bus = Button(root, image=search_bus_img, bd=0, bg="#ffd5bc", activebackground="#ffd5bc", command=SearchBus)
search_bus.place(x=580, y=540)

# Add Bus App Button Image (Global)
add_btn = ImageTk.PhotoImage(Image.open("./Assets/add_bus_child.png"))

# Search Bus App Button Image (Global)
src_btn = ImageTk.PhotoImage(Image.open("./Assets/search_bus_child.png"))

# Home Button (Global)
home_btn = ImageTk.PhotoImage(Image.open("./Assets/home.png"))

# Add Details Button (Global)
add_det_btn = ImageTk.PhotoImage(Image.open("./Assets/add_details_btn.png"))

# Icon Photo (Global)
icon_photo = PhotoImage(file = "./Assets/root_icon.png")

#********************************************** DATABASE *************************************************#
conn = sqlite3.connect('bus_list.db')
c = conn.cursor()
c.execute('''create table if not exists Operator_Details (Full_name vauchar(50) not null, Contact_no int(10) not null, Address varchar(50) not null)''')
c.execute('''create table if not exists Bus_Details (Agency_name varchar(50) not null, Bus_type varchar(30) not null, loc_From varchar(30) not null, loc_To varchar(30) not null, Date date, Dep_Time time, Arrival_Time time, fare int(10), seats int(10))''')
conn.commit()
conn.close()

def Add_Bus_Record(Agency_name, Bus_type, loc_From, loc_To, Date, Dep_Time, Arrival_Time, fare, seats):
    conn = sqlite3.connect('bus_list.db')
    c = conn.cursor()
    c.execute("INSERT INTO Bus_Details VALUES (?,?,?,?,?,?,?,?,?)", (Agency_name, Bus_type, loc_From, loc_To, Date, Dep_Time, Arrival_Time, fare, seats))
    conn.commit()
    conn.close()

def Add_Operator_Record(Full_name, Contact_no, Address):
    conn = sqlite3.connect('bus_list.db')
    c = conn.cursor()
    c.execute("INSERT INTO Operator_Details VALUES (?,?,?)", (Full_name, Contact_no, Address))
    conn.commit()
    conn.close()

def Search_Bus(loc_From, loc_To, date):
    conn = sqlite3.connect('bus_list.db')
    c = conn.cursor()
    c.execute("select * from Bus_Details where loc_From=(?) and loc_To=(?) and date=(?)", (loc_From, loc_To, date,))
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows
#********************************************** DATABASE END*************************************************#
root.mainloop()
