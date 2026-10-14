# student marks

import csv

with open("marks.csv","w",newline="")as file:
    write=csv.writer(file)
    write.writerow(["name","marks"])
    write.writerow(["ravi",85])
    write.writerow(["priya",92])

print("csv created")