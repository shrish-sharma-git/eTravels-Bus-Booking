import sqlite3

def BusData():
    conn = sqlite3.connect('bus_list.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE if not exists BusList(Agency_Name varchar(30) not null, Contact_Number int(10) not null, Address varchar(30) not null, Operator_Id int(10) not null, Bus_Type varchar(15) not null, loc_From varchar(50) not null, loc_To varchar(50) not null, Departure_Time varchar(10) not null, Arrival_Time varchar(10) not null, fare int(10), num_seats int(50) not null, primary key(Operator_Id))""")
    conn.commit()
    conn.close()
