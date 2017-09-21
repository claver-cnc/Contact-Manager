class Contact:
    def __init__(self, name, phoneNumber, email):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email

    def __repr__(self):
        return "String representation of contact"

class ContactManager:
    def __init__(self, contacts=[]):
        self.contacts = contacts

    def addContact(self):
        myName = input("\nEnter the name of your contact: ")
        myNum = input("Enter the phone number of your contact: ")
        myMail = input("Enter the email of this person: ")
        self.contacts.append(Contact(myName, myNum, myMail))

    def delete(self):
        toDelete = input("\n Enter the name of contact your want to delete: ")
        for listContact in self.contacts:
            if listContact.name == toDelete:
                self.contacts.remove(listContact)
                print("\n Contact Delected")
        return None

    def search(self):
        toSearch = input("\n Enter the name of your want to search: ")
        found = 0
        for listContact in self.contacts:
            if listContact.name == toSearch:
                print("Name= " + listContact.name + " | Contact= " + listContact.phoneNumber + " | Email= " + listContact.email)
                found = 1
        if found == 0:
            print("Sorry this contact doesn't existed")


boucle = 0
print("      \n         Welcome Guy !! \n" \
      "\nEnter the number of your operation " )

while boucle == 0:

    print("\n1- Add one number " \
          "\n2- Delete one number " \
          "\n3- Search a contact " \
          "\n4- Show all the contacts" \
          "\n5- Exit")

    choice = input()
    newcontact = ContactManager()

    if choice == "1":
        add = 0
        while add == 0:
            newcontact.addContact()
            fiche = open("contact.txt", "a")
            for listContact in newcontact.contacts:
                fiche.write("Name= "+listContact.name+" | Contact= "+listContact.phoneNumber + " | Email= "+listContact.email+"\n")
            fiche.close()
            answer = input("Would you want to add a new contact ? Yes || No \n")
            if answer != "Yes":
                add = 1

    elif choice == "2":
        newcontact.delete()

    elif choice == "3":
        newcontact.search()

    elif choice == "4":
        for listContact in newcontact.contacts:
            print("Name= "+listContact.name+" | Contact= "+listContact.phoneNumber + " | Email= "+listContact.email)

    elif choice == "5":
        boucle = 1

    else:
        print("Make one real choice")

