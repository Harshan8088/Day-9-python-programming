total=0

with open("expense.txt","r")as file:
    for line in file:
        item,amount=line.strip().rsplit(",",1)
        total +=float(amount)

    print("total expenses:Rs.",total)