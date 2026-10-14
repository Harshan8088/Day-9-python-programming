# daily expense recordd
item=input("expense description:")
amount=float(input("amount:"))

with open("expense.txt","a")as file:
    file.write(f"{item},{amount}\n")

print("expense recorded")
