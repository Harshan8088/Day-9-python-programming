# read csv data

import csv

with open("marks.csv","r",newline="")as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
