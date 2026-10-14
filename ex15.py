name=input("employ name:")
salary=float(input("salary:"))

with open("employees.txt","a")as file:
    file.write("f{name},{salary}\n")
print("employee record saved")