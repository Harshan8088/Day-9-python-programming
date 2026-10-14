# student multiple student names

n=int(input("number of student:"))

with open ("students.txt","w")as file:
    for i in range (n):
        name=input("enter name:")
        file.write(name+"\n")

print("all student saved")