def add_note():
    note =input("write your note:")

    with open("my_noted.txt","a")as file:
        file.write(note+"\n")

    print("note saved")

def view_notes():
    try:
        with open("my_notes.txt","r")as file:
            print("\n--YOUR NOTES--")
            print(file.read())
    except FileNotFoundError:
        print("no notes avaliable")

while True:
    print("\n--NOTE APP---")
    print("1.add note")
    print("2.view notes")
    print("2.exit")

    choice=input("choose:")

    if choice=="1":
            add_note()
    elif choice=="2":
            view_notes()
    elif choice=="3":
        break
    else:
        print("invalid choice")
