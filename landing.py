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
    add_bus_app.resizable(0,0)
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
    txtFull_name.grid(row=2, column=1, padx=50, pady=5)

    txtContact_Number = Entry(add_bus_app, width=60, textvariable=Contact_no)
    txtContact_Number.grid(row=3, column=1, pady=5)

    txtAddress = Entry(add_bus_app, width=60, textvariable=Address)
    txtAddress.grid(row=4, column=1, pady=5)

    
    # Adding Entry Labels
    Full_name_label = Label(add_bus_app, text="Full Name", font=('PSBold', 10), fg='#fff', bg='#D1456E')
    Full_name_label.grid(row=2, column=0, padx=50)

    Contact_Number_label = Label(add_bus_app, text="Contact Number", font=('PSBold', 10), fg='#fff', bg='#D1456E')
    Contact_Number_label.grid(row=3, column=0)

    Address_label = Label(add_bus_app, text="Address", font=('PSBold', 10), fg='#fff', bg='#D1456E')
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
        txtAgency_Name.grid(row=6, column=1, pady=5, padx=10)

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
        Agency_name_label = Label(add_bus_app, text="Agency Name", font=('PSBold', 10), fg='#fff', bg='#D1456E')
        Agency_name_label.grid(row=6, column=0)

        Bus_Type_label = Label(add_bus_app, text="Bus Type", font=('PSBold', 10), fg='#fff', bg='#D1456E')
        Bus_Type_label.grid(row=7, column=0)

        loc_From_label = Label(add_bus_app, text="From Location", font=('PSBold', 10), fg='#fff', bg='#D1456E')
        loc_From_label.grid(row=8, column=0)

        loc_To_label = Label(add_bus_app, text="To Loaction", font=('PSBold', 10), fg='#fff', bg='#D1456E')
        loc_To_label.grid(row=9, column=0)

        date_label = Label(add_bus_app, text="Date", font=('PSBold', 10), fg='#fff', bg='#D1456E')
        date_label.grid(row=10, column=0)
        
        Dep_Time_label = Label(add_bus_app, text="Departure Time", font=('PSBold', 10), fg='#fff', bg='#D1456E')
        Dep_Time_label.grid(row=11, column=0)

        Arrival_Time_label = Label(add_bus_app, text="Arrival TIme", font=('PSBold', 10), fg='#fff', bg='#D1456E')
        Arrival_Time_label.grid(row=12, column=0)

        Fare_label = Label(add_bus_app, text="$ Fare", font=('PSBold', 10), fg='#fff', bg='#D1456E')
        Fare_label.grid(row=13, column=0)

        Seats_label = Label(add_bus_app, text="Total Seats", font=('PSBold', 10), fg='#fff', bg='#D1456E')
        Seats_label.grid(row=14, column=0)

        # The Add Bus Button (2nd on Add Bus Page)
        submit_btn = Button(add_bus_app, image=add_btn, bd=0, bg='#D1456E', command=Add_Record).grid(row=15, column=1)

    def Add_Record():
        if(len(Agency_name.get()) != 0):
            Add_Bus_Record(Agency_name.get(), Bus_type.get(), loc_From.get(), loc_To.get(), Date.get(), Dep_Time.get(), Arrival_Time.get(), fare.get(), seats.get())
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
    search_bus_app.resizable(0,0)
    search_bus_app.iconphoto(False, icon_photo)

    # image as a background for Add Bus
    load_src_bg = Image.open('./Assets/search_bus_bg.png')
    render_src_bus = ImageTk.PhotoImage(load_src_bg)
    img_src_bus = Label(search_bus_app, image=render_src_bus)
    img_src_bus.image = render_src_bus
    img_src_bus.place(x=0, y=0)

    labelExample = Label(search_bus_app, text = "Welcome Visitor!", font=('PSBold', 18), bg='#D1456E', fg='#fff').grid(row=0, column=1, pady=10)

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
    bus_type_dropd.config(width = 40, bg='#D1456E', fg="#fff")
    bus_type_dropd.grid(row=3, column=1, pady=30)

    # Labels
    loc_From_label = Label(search_bus_app, text="From Location", font=('PSBold', 10), fg='#fff', bg='#D1456E')
    loc_From_label.grid(row=5, column=0, padx=50)

    loc_To_label = Label(search_bus_app, text="To Loaction", font=('PSBold', 10), fg='#fff', bg='#D1456E')
    loc_To_label.grid(row=6, column=0, padx=10)

    date_label = Label(search_bus_app, text="Date", font=('PSBold', 10), fg='#fff', bg='#D1456E')
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

    #Search Function
    def Search():
        if(str(loc_From.get()) != 0 and str(loc_From.get()) != str(loc_To.get())):
            search_app = Toplevel()
            search_app.geometry('800x700+300+50')
            search_app.resizable(0,0)
            # image as a background for Add Bus
            load_src_bg = Image.open('./Assets/results_bg.png')
            render_src_bus = ImageTk.PhotoImage(load_src_bg)
            img_src_bus = Label(search_app, image=render_src_bus)
            img_src_bus.image = render_src_bus
            img_src_bus.place(x=0, y=0)

            # Fetching And Showing Details.
            conn = sqlite3.Connection('bus_list.db')
            c = conn.cursor()
            Agency_name_label=Label(search_app,text="Name",font=('PSBold', 15), fg='#fff', bg='#D1456E',padx=5, pady=15).grid(row=0,column=0)
            Bus_Type_label=Label(search_app,text="Type",font=('PSBold', 15), fg='#fff', bg='#D1456E',padx=5, pady=15).grid(row=0,column=1)
            loc_From_label=Label(search_app,text="From",font=('PSBold', 15), fg='#fff', bg='#D1456E',padx=5, pady=15).grid(row=0,column=2)
            loc_To_label=Label(search_app,text="To",font=('PSBold', 15), fg='#fff', bg='#D1456E',padx=5, pady=15).grid(row=0,column=3)
            date_label=Label(search_app,text="Date",font=('PSBold', 15), fg='#fff', bg='#D1456E',padx=5, pady=15).grid(row=0,column=4)
            Dep_Time_label=Label(search_app,text="Departure On",font=('PSBold', 15), fg='#fff', bg='#D1456E',padx=5, pady=15).grid(row=0,column=5)
            Arrival_Time_label=Label(search_app,text="Arrival On",font=('PSBold', 15), fg='#fff', bg='#D1456E',padx=5, pady=15).grid(row=0,column=6)
            Fare_label=Label(search_app,text="Fare",font=('PSBold', 15), fg='#fff', bg='#D1456E',padx=5, pady=15).grid(row=0,column=7)
            Seats_label=Label(search_app,text="Seat(s)",font=('PSBold', 15), fg='#fff', bg='#D1456E',padx=5, pady=15).grid(row=0,column=8)
            Select_label=Label(search_app,text="Book",font=('PSBold', 15), fg='#fff', bg='#D1456E',padx=5, pady=15).grid(row=0,column=9)
            
            d_click = click.get()
            l_from = loc_From.get()
            l_to = loc_To.get()
            d_date = date.get()
            c.execute("SELECT * FROM Bus_Details WHERE loc_From=(?) and loc_To=(?) and Date=(?)",(l_from,l_to,d_date,))
            res_data = c.fetchall()
            conn.close()
            print(res_data)
            num=3
            x=1
            for row in res_data:
                print(row)
                v=IntVar()
                name=Label(search_app,text=row[0], font=('PSBold', 10), fg='#fff', bg='#D1456E').grid(row=num, column=0)
                b_type=Label(search_app,text=row[1], font=('PSBold', 10), fg='#fff', bg='#D1456E').grid(row=num,column=1)
                l_frm=Label(search_app,text=row[2], font=('PSBold', 10), fg='#fff', bg='#D1456E').grid(row=num,column=2)
                l_to=Label(search_app,text=row[3], font=('PSBold', 10), fg='#fff', bg='#D1456E').grid(row=num,column=3)
                l_date=Label(search_app,text=row[4], font=('PSBold', 10), fg='#fff', bg='#D1456E').grid(row=num,column=4)
                dep_t=Label(search_app,text=row[5], font=('PSBold', 10), fg='#fff', bg='#D1456E').grid(row=num,column=5)
                arr_t=Label(search_app,text=row[6], font=('PSBold', 10), fg='#fff', bg='#D1456E').grid(row=num,column=6)
                l_fare=Label(search_app,text=row[7], font=('PSBold', 10), fg='#fff', bg='#D1456E').grid(row=num,column=7)
                l_seat=Label(search_app,text=row[8], font=('PSBold', 10), fg='#fff', bg='#D1456E').grid(row=num,column=8)
                radio_btn=Radiobutton(search_app,variable=v,value=x, bg='#D1456E')
                radio_btn.grid(row=num,column=9) 
                x+1
                num=num+1
            def book_tickets():
                res = v.get()
                print(res)
                if res == 1:
                    messagebox.showinfo("Success!!", "Your Seats Has Been Booked!")
                else:
                    messagebox.showerror("Sorry!", "You have to select your ride first!", parent=search_app)
                
                
            Book_btn = Button(search_app, text="Book Seats", command=book_tickets, bd=5, bg="#871e3d", fg="#fff").grid(column=9, sticky='nw', ipadx=10, ipady=5, pady=10)
        else:
            messagebox.showerror("Error!", "Please Make Sure to Fill all the Input Fields Correctly!")
    
                
    # Search Button
    search_btn = Button(search_bus_app, image=src_btn, bd=0, bg='#D1456E', command=Search).place(x=270, y=240)

    #Delete Database Button(Resetting The Database)
    def Delete():
        response = messagebox.askyesno("Warning", "Are you sure you want to delete the database?", parent=search_bus_app)
        if response == True:            
            conn = sqlite3.connect('bus_list.db')
            c=conn.cursor()
            c.execute("DELETE FROM Bus_Details")
            conn.commit()
            messagebox.showinfo("Success!", "Database Deleted Successfully!", parent=search_bus_app)
        else:
            messagebox.showinfo("REQUEST ABORTED!", "Your Database Was Not Deleted.", parent=search_bus_app)
    del_btn = Button(search_bus_app, image=delete_btn, bd=0, bg='#D1456E', command=Delete).place(x=150, y=635)
    

#********************* SEARCH BUS WINDOW ENDS************************************************************    
    

# Buttons
label_add = Label(root, text='(For Operators)', font=('PSBold', 15), bg="#ffd5bc")
label_add.place(x=35, y=500)
label_search = Label(root, text='(For Customers)', font=('PSBold', 15), bg="#ffd5bc")
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

# Add Details Button (Global)
delete_btn = ImageTk.PhotoImage(Image.open("./Assets/del_btn.png"))

# Icon Photo (Global)
icon_photo = PhotoImage(file = "./Assets/root_icon.png")

# Handling The CLosing Protocol
def on_closing():
    if messagebox.askokcancel("Quit!", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

#********************************************** DATABASE *************************************************#
conn = sqlite3.connect('bus_list.db')
c = conn.cursor()
c.execute('''create table if not exists Operator_Details (Full_name vauchar(50) not null, Contact_no int(10) not null, Address varchar(50) not null)''')
c.execute('''create table if not exists Bus_Details (Agency_name varchar(50) not null, Bus_type varchar(30) not null, loc_From varchar(30) not null, loc_To varchar(30) not null, Date date, Dep_Time time, Arrival_Time time, fare int(10), seats int(10))''')
conn.commit()
conn.close()

# Adding Bus Details
def Add_Bus_Record(Agency_name, Bus_type, loc_From, loc_To, Date, Dep_Time, Arrival_Time, fare, seats):
    conn = sqlite3.connect('bus_list.db')
    c = conn.cursor()
    c.execute("INSERT INTO Bus_Details VALUES (?,?,?,?,?,?,?,?,?)", (Agency_name, Bus_type, loc_From, loc_To, Date, Dep_Time, Arrival_Time, fare, seats))
    conn.commit()
    conn.close()

# Adding Operator Details
def Add_Operator_Record(Full_name, Contact_no, Address):
    conn = sqlite3.connect('bus_list.db')
    c = conn.cursor()
    c.execute("INSERT INTO Operator_Details VALUES (?,?,?)", (Full_name, Contact_no, Address))
    conn.commit()
    conn.close()
#********************************************** DATABASE END*************************************************#
root.mainloop()
