# search student name

name=input("search student:").strip()

with open("students.txt","r")as file:
students=[line.strip()for line in file]

if name.lower() in [s.lower()for s in students]:
    print("student found")
else:
    print("student not found")