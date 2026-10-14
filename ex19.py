# handle missing file

try:
    with open("report.txt","r")as file:
        print(file.read())

except FileNotFoundError:
    print("filr does not exist")