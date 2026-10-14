# save student name

name=input("enter student name:")

with open("student.txt","w")as file:
    file.write(name)

print("student name saved")