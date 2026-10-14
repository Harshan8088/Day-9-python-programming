# read JSON data

import json

with open("student.json","r")as file:
    student=json.load(file)

print("name:",student["name"])
print("course:",student["course"])