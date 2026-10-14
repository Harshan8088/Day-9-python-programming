# cound number of lines

with open("subjects.txt","r")as file:
    line=file.readlines()

print("total lines:",len(line))