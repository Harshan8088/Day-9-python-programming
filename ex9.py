# count characters

with open("welcome.txt","r")as file:
    content=file.read()

print("characters:",len(content))