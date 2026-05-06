phonebook = {"AMIT": "9876543210","RIYA":"9123456780"}
# add contact
def add_contact():
    name = input("enter name:").upper()
    if name in phonebook:
        print("contact already eists!")
    else:
        number = input("enter phone number:")
        phonebook[name] = number
        print("contact added successfully")
# search add contact
def search_contact():
    name = input("enter name to search :").upper()
    found = False
    for key in phonebook:
        if name in key:
            print(f"{key} :{phonebook[key]}")
            found  = True
    if not found:
        print("contact not found")
# delete contact
def delete_contact():
    name = input("enter name to delete:").upper()
    if name in phonebook:
        del phonebook[name]
        print("contact deleted")
    else:
        print("contact not found")
# display all contacts
def display_contact():
    if not phonebook:
        print("phonebook is empty")
    else:
        print("\n phonebook contacts:")
        for name, number in phonebook.items():
            print(f"{name} :{number}")

while True:
    print("\n___ PHONEBOOK MENU ___")
    print("1. Add contact")
    print("2. search contact")
    print("3. delete contact")
    print("4. display all contacts")
    print("5. exit")
    choice = input("enter your choice:")
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        display_contact()
    elif choice == "5":
        print("existing program")
        break
    else:
        print("invalid choice ! try again.")