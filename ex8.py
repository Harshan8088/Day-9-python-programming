# count words in a file

with open("welcome.txt","r")as file:
    content=file.read()

words=content.split()
print("total words:",len("words"))