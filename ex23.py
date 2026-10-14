# save dictionary as JSON
import json
student={
    "name":"rahul",
    "age":20,
    "course":"python"
}

with open("student.json","w")as file:
    json.dump(student,file,indent=4)

print("JSON saved")