# Define a list to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print("Contact added successfully!")

# Function to view contact list
def view_contact_list():
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        print("Contact List:")
        for i, contact in enumerate(contacts):
            print(f"{i+1}. Name: {contact['name']}, Phone: {contact['phone']}")

# Function to search for a contact
def search_contact():
    search_term = input("Enter a name or phone number to search for: ")
    results = []
    for contact in contacts:
        if search_term in contact["name"] or search_term in contact["phone"]:
            results.append(contact)
    if len(results) == 0:
        print("No matching contacts found.")
    else:
        print("Matching Contacts:")
        for i, contact in enumerate(results):
            print(f"{i+1}. Name: {contact['name']}, Phone: {contact['phone']}")

# Function to update a contact
def update_contact():
    view_contact_list()
    if len(contacts) == 0:
        return
    contact_index = int(input("Enter the index of the contact to update: ")) - 1
    if 0 <= contact_index < len(contacts):
        contact = contacts[contact_index]
        print("Update Contact:")
        name = input(f"Enter new name for {contact['name']}: ")
        phone = input(f"Enter new phone number for {contact['phone']}: ")
        email = input(f"Enter new email for {contact['email']}: ")
        address = input(f"Enter new address for {contact['address']}: ")
        contact.update({"name": name, "phone": phone, "email": email, "address": address})
        print("Contact updated successfully!")

# Function to delete a contact
def delete_contact():
    view_contact_list()
    if len(contacts) == 0:
        return
    contact_index = int(input("Enter the index of the contact to delete: ")) - 1
    if 0 <= contact_index < len(contacts):
        deleted_contact = contacts.pop(contact_index)
        print(f"Contact '{deleted_contact['name']}' deleted successfully!")

# Main menu
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact_list()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting the Contact Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
