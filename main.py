import tkinter
import mysql.connector


def insert_data():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nirmalkumar5#",
        port="3306",
        database="hotel_management"
    )
    Id = int(id_entry.get())
    Name = name_entry.get()
    Age = int(age_entry.get())
    Gender = gender_entry.get()
    People = int(people_entry.get())
    Room = int(room_entry.get())
    Amount = int(Amount_entry.get())

    cursor = db.cursor()
    cursor.execute(f"insert into hotelmanagement values({Id},'{Name}',{Age},'{Gender}',{People},{Room},{Amount})")
    db.commit()
    print("success")
def estimating():
    Amount=int(room_entry.get())*1000
    Amount_entry.insert(0,str(Amount))

FONT = ("times new roman", 30, "bold")
window = tkinter.Tk()

window.title("Hotel Management")
logo_img1 = tkinter.PhotoImage(file="hotel_logo.png")

frame1 = tkinter.Frame(width=300, height=400)
frame1.pack(side="left")
frame1_1 = tkinter.Label(master=frame1, image=logo_img1)
frame1_1.pack(side="top", padx=20)

frame2 = tkinter.Frame(width=500, height=400)
frame2.pack(side="left")
frame1_2 = tkinter.Frame(master=frame1)
frame1_2.pack(side="top")

title_label = tkinter.Label(frame1_2, text="\nHotel\ndatabase", font=FONT)
title_label.pack(side="top")

logo_label = tkinter.Label(master=frame1_2)

id_label = tkinter.Label(frame2, text="Id:", font=FONT, pady=10)
id_label.grid(row=0, column=0)
id_entry = tkinter.Entry(frame2, font=FONT)
id_entry.grid(row=0, column=1, columnspan=2)

name_label = tkinter.Label(frame2, text="Name:", font=FONT, pady=10)
name_label.grid(row=1, column=0)
name_entry = tkinter.Entry(frame2, font=FONT)
name_entry.grid(row=1, column=1, columnspan=2)

age_label = tkinter.Label(frame2, text="Age:", font=FONT, pady=10)
age_label.grid(row=2, column=0)
age_entry = tkinter.Entry(frame2, font=FONT)
age_entry.grid(row=2, column=1, columnspan=2)

gender_label = tkinter.Label(frame2, text="Gender:", font=FONT, pady=10)
gender_label.grid(row=3, column=0)
gender_entry = tkinter.Entry(frame2, font=FONT)
gender_entry.grid(row=3, column=1, columnspan=2)

people_label = tkinter.Label(frame2, text="People:", font=FONT, pady=10)
people_label.grid(row=4, column=0)
people_entry = tkinter.Entry(frame2, font=FONT)
people_entry.grid(row=4, column=1, columnspan=2)

room_label = tkinter.Label(frame2, text="Room:", font=FONT, pady=10)
room_label.grid(row=5, column=0)
room_entry = tkinter.Entry(frame2, font=FONT)
room_entry.grid(row=5, column=1, columnspan=2)

Amount_label = tkinter.Label(frame2, text="Amount:", font=FONT, pady=10)
Amount_label.grid(row=6, column=0)
Amount_entry = tkinter.Entry(frame2, font=FONT)
Amount_entry.grid(row=6, column=1, columnspan=2)

estimate_button = tkinter.Button(frame2, text="Estimate", font=FONT,command=estimating)
estimate_button.grid(row=7, column=1)

submit_button = tkinter.Button(frame2, text="Submit", font=FONT,command=insert_data)
submit_button.grid(row=7, column=2)

window.mainloop()
