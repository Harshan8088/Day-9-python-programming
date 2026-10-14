# generate shopping bill
customer=input("customer name:")
product=input("product name:")
price=float(input("price:"))
quentity=int(input("quentity"))

total=price*quentity

with open("bill.txt","w")as file:
    file.write("SHOPPING BILL\n")
    file.write(f"customer:{customer}\n")
    file.write(f"product:{product}\n")
    file.write(f"quentity:{quentity}\n")
    file.write(f"Total:Rs.{total:2f}\n")

print("Bill generate successfully")