# append file line by line
with open("subjects.txt","a")as file:
    file.write("database mangement\n")

print("new subject added")

# read first line

with open ("subjects.txt","r")as file:
    first_line=file.readline()

print(first_line.strip())