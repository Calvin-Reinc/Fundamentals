# Task 5: Write a program that creates a simple phone book using a dictionary (or object in JavaScript). 
# Allow the user to add new contacts, delete contacts, and search for a contact by name.
phoneList = {}


def add_phonebook():
    
    myBool = True
    while myBool:
        try:
            userName = str(input("Enter your name: "))
            userNumber = str(input("Enter a number: (Make sure your number is correct): "))
            update = {userName: userNumber}
            myBool = False
        except:
            print("An error occured")
    phoneList.update(update)
    return userName, userNumber


def delete_phone(userName):
    return phoneList.pop(userName)


def search_phone():
    lookFor = str(input("What's the name of the contact: "))
    print("Searching", end="")
    for i in range(4):
        print(".", end="")
        
    print("")
    try:
        print(f"{lookFor} - {phoneList[lookFor]}")
        print("Contact found.")
    except:
        print("Contact not found.")


def view_phone():
    for key, value in phoneList.items():
        print(f"Name: {key} & Number: {value}")
        
        
if __name__ == "__main__":
    print("---- Phonebook ----")

    myBool = True
    while myBool:
        print("1. Add new contact"+"\n"+"2. Delete contact"+"\n"+"3. Search"+"\n"+"4. Display contacts"+"\n"+"Q to quit")
        work = input("select option(Use numbers): ")
        if work[0] == "1":
            userName, userNumber = add_phonebook()
            print(f"{userName}:  {phoneList[userName]}\n Contact saved.")
        elif work[0] == "2":
            userName = input("Search by name: ")
            delete_phone(userName)
            print("Contact deleted!")
        elif work[0] == "3":
            search_phone()
        elif work[0].capitalize() == "Q":
            myBool = False
        elif work[0] == "4":
            view_phone()
        else:
            print("Select a valid option.(Use number to identify)")