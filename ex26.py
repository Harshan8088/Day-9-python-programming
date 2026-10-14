# daily  attendence system

import csv
from datetime import date

def mark_attendence():
    roll=input("roll number :")
    name=input("student name:")
    status=input("present/absent(p/a):").upper()

    if status not in ("P","A"):
        print("invalid status")
        return

    with open("attendance.csv","a",newline="")as file:
        write=csv.write(file)
        write.writerow([
            str(date.today()),
            roll,
            name,
            status
        ])

    print("attendence saved")

def view_attendence():
    try:
        with open("attendence.csv","r",newline="")as file:
            reader=csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("no attendence records")


while True:
    print("\1.Marks attendence")
    print("2.View attendence")
    print("3.exit")

    choice=input("enter choice:")

    if choice=="1":
        mark_attendence()
    elif choice=="2":
        view_attendence()
    elif choice=="3":
        break
    else:
        print("invalid choice")