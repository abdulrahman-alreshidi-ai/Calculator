import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


contacts = load_contacts()


while True:

    print("\n========== Contact Book ==========")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":

        if not contacts:
            print("No contacts found.")

        else:
            print("\nContacts:")
            for contact in contacts:
                print(f"Name : {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print("-" * 25)

    elif choice == "2":

        name = input("Name : ")
        phone = input("Phone: ")

        contacts.append({
            "name": name,
            "phone": phone
        })

        save_contacts(contacts)

        print("Contact added successfully.")

    elif choice == "3":

        keyword = input("Enter name: ").lower()

        found = False

        for contact in contacts:

            if keyword in contact["name"].lower():

                print(f"\nName : {contact['name']}")
                print(f"Phone: {contact['phone']}")
                found = True

        if not found:
            print("Contact not found.")

    elif choice == "4":

        name = input("Enter name to delete: ").lower()

        deleted = False

        for contact in contacts:

            if contact["name"].lower() == name:
                contacts.remove(contact)
                save_contacts(contacts)
                deleted = True
                print("Contact deleted.")
                break

        if not deleted:
            print("Contact not found.")

    elif choice == "5":

        print("Goodbye.")
        break

    else:
        print("Invalid choice.")
