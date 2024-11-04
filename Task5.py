# TASK 5 : CONTACT BOOK...

contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print(f"Contact '{name}' added.")

def view_contacts():
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"  Phone: {info['Phone']}")
            print(f"  Email: {info['Email']}")
            print(f"  Address: {info['Address']}")
            print("-" * 20)
    else:
        print("No contacts found.")

def search_contact():
    search_name = input("Enter the name to search: ")
    if search_name in contacts:
        info = contacts[search_name]
        print(f"Name: {search_name}")
        print(f"  Phone: {info['Phone']}")
        print(f"  Email: {info['Email']}")
        print(f"  Address: {info['Address']}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        address = input("Enter new address: ")
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print(f"Contact '{name}' updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")

def contact_book():
    while True:
        print("\nContact Book Options:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    contact_book()
