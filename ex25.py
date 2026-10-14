# student record management

import csv
import os
FILENAME="student_record.csv"

def add_student():
    roll=input("roll number:")
    name=input("student name:")
    course=input("course:")

    with open(FILENAME,"a",newline="")as file:
        write=csv.writer(file)
        write.writerow([roll,name,course])

    print("student added")

def view_students():
    if not os.path.exists(FILENAME):
        print("no records found")
        return

    with open(FILENAME,"r",newline="")as file:
        reader=csv.reader(file)
        for row in reader:
            if len(row)==3:
                print("roll:",row[0],
                "name:",row[1],
                "course:",row[2])


def search_student():
    roll=input("enter roll number:")

    if not os.path.exists(FILENAME):
        print("NO RECORE FOUND")
        return

    with open(FILENAME,"r",newline="")as file:
        reader=csv.reader(file)
        for row in reader:
            if len(row)==3 and row[0]==roll:
                print("student found:",row)
                return

    print("student not found")

while True:
    print("\n---STUDENT RECORD SYSTEM---")
    print("1.add student")
    print("2.view student")
    print("3.search student")
    print("4.exit")


    choice=input("choose option:")

    if choice=="1":
        add_student()
    elif choice=="2":
        view_students()
    elif choice=="3":
        search_student()
    elif choice=="4":
        break
    else:
        print("invalid choice")