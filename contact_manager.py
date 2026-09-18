import sys

def add_contact(contacts,contact_keys):
    '''Adds a new contact to the contacts list after validation '''
    print("\n--- ADD NEW CONTACT (Type 'cancel' to return to menu) ---")
    name = input("Enter Name (Required)(or 'cancel'): ")
    if name.lower() == "cancel":
        print("Operation cancelled.Returning to the main menu...")
        return
    if name == "":
        print("Error: Name cannot be empty. Operation cancelled.")
        return
    # Loop for phone number validation
    while True:
        phone = input("Enter Phone Number (11 digits Required)(or 'cancel'): ")
        if phone.lower() == "cancel":
            print("Operation cancelled.Returning to the main menu...")
            return
        # Check if phone number is exactly 11 digits and contain only numeric characters.
        if len(phone)!=11 or (phone.isdigit() != True):
            print("ERROR: Phone number must be exactly 11 digits and contain only numbers (no dashes or spaces)")
            continue
        break
    email = input("Enter Email(or 'cancel'): ")
    if email.lower() == "cancel":
        print("Operation cancelled.Returning to the main menu...")
        return
    if email == "":
        print("Error: Email cannot be empty. Operation cancelled.")
        return
    country = input("Enter Country(or 'cancel'): ")
    if country.lower() == "cancel":
        print("Operation cancelled.Returning to the main menu...")
        return
    if country == "":
        print("Error: Country cannot be empty. Operation cancelled.")
        return
    '''Add to contact list with immutable key structure'''
    contact={contact_keys[0]: name, contact_keys[1]: phone, contact_keys[2]: email, contact_keys[3]: country}
    contacts.append(contact)
    print(f"Contact added successfully: {name}")
    return

def view_contacts(contacts,contact_keys):
    """Displays all contacts in a formatted list."""
    print("\n--- CONTACT LIST ---")
    if len(contacts) == 0:
        print("No contacts found.")
        return

    '''Dynamic Tuple Header Part '''
    print("===================================================================================")
    print("Index|", end="")
    for contact_key in contact_keys:
        print(f" {contact_key.capitalize()}            |", end="")
    print("\n===================================================================================")
    for i, current_contact in enumerate(contacts, 1):
        print(f"{i}    | {current_contact['name']}       | {current_contact['phone']}    | {current_contact['email']}    | {current_contact['country']}    |")
    return

def find_contact(contacts,name,contact_keys):
    """Finds and returns all contacts that match a given name."""
    matches = [contact for contact in contacts if name.lower() in contact[contact_keys[0]].lower()]
    return matches

def edit_contact(contacts,contact_keys):
    """Allows user to edit an existing contact."""
    print("\n--- EDIT CONTACT (Type 'cancel' to return to menu) ---")
    name = input("Enter the name (or part of the name) of the contact to edit(or 'cancel'): ")
    if name.lower() == "cancel":
        print("Operation cancelled.Returning to the main menu...")
        return
    matches = find_contact(contacts, name,contact_keys)
    if len(matches) == 0:
        print(f"No contacts found matching '{name}'.")
        return
    """ Valuable for only one contact situation """
    if len(matches) == 1:
        choice = 1
    # Multiple matches
    if len(matches) > 1:
        print("Multiple contacts found. Please select one to edit or 'cancel' to cancel the edit.:")
        for i, match in enumerate(matches,1):
            # Matching value with tuple key structure
            print(f"[{i}] {match[contact_keys[0]]} ({match[contact_keys[1]]})")
        choice = input("Contact number to edit(or cancel): ")
        if choice.lower() == "cancel":
            print("Operation cancelled.Returning to the main menu...")
            return
        if int(choice) < 1 or int(choice) > len(matches):
            print("ERROR: Invalid choice.")
            return
    contact = matches[int(choice) - 1]

    print("\n----CONTACT UPDATE----")
    print("Which field do you want to change?")
    print("[1] Current name:", contact['name'])
    print("[2]Current phone:", contact['phone'])
    print("[3]Current email:", contact['email'])
    print("[4]Current country:", contact['country'])
    print("Cancel")
    preference = input("Enter preference(1,4) or 'cancel':")
    if preference == "cancel":
        print("Operation cancelled.Returning to the main menu...")
        return
    elif preference == "1":
        new_val = input("Enter new name(or 'cancel'):")
        if new_val.lower() == "cancel":
            print("Update cancelled.Returning to the main menu...")
            return
        if new_val == "":
            print("Error: Name cannot be empty. Operation cancelled.")
            return
        contact[contact_keys[0]] = new_val
        change="name"
    elif preference == "2":
        # Loop for phone number validation
        while True:
            new_val = input("Enter new phone (11 digits) (or 'cancel'): ")
            if new_val.lower() == "cancel":
                print("Update cancelled.Returning to the main menu...")
                return
            # Check if phone number is exactly 11 digits and contain only numeric characters.
            if len(new_val) != 11 or (new_val.isdigit() != True):
                print("ERROR: Phone number must be exactly 11 digits and contain only numbers (no dashes or spaces)")
                continue
            contact[contact_keys[1]] = new_val
            break
        change = "phone"
    elif preference == "3":
        new_val = input("Enter new email (or 'cancel'):")
        if new_val.lower() == "cancel":
            print("Update cancelled.Returning to the main menu...")
            return
        if new_val == "":
            print("Error: Email cannot be empty. Operation cancelled.")
            return
        contact[contact_keys[2]] = new_val
        change = "email"
    elif preference == "4":
        new_val = input("Enter new country (or 'cancel'):")
        if new_val.lower() == "cancel":
            print("Update cancelled.Returning to the main menu...")
            return
        if new_val == "":
            print("Error: Country cannot be empty. Operation cancelled.")
            return
        contact[contact_keys[3]] = new_val
        change = "country"
    else:
        print("ERROR: Invalid preference.")
        return
    print(f"Success! {contact[contact_keys[0]]} {change} updated to {new_val}.")
    return

def delete_contact(contacts,contact_keys):
    """Deletes a selected contact."""
    print("\n--- DELETE CONTACT (Type 'cancel' to return to menu)---")
    name = input("Enter the name (or part of the name) of the contact to delete(or 'cancel'): ")
    if name.lower() == "cancel":
        print("Operation cancelled.Returning to the main menu...")
        return
    matches = find_contact(contacts, name,contact_keys)
    if len(matches) == 0:
        print(f"No contacts found matching '{name}'.")
        return

    """ Valuable for only one contact situation """
    if len(matches) == 1:
        choice = 1
    # Multiple matches
    if len(matches) > 1:
        print("Multiple contacts found. Please select one to delete or type '0' to cancel the delete.:")
        for i, match in enumerate(matches, 1):
            # Matching value with tuple key structure
            print(f"[{i}] {match[contact_keys[0]]} ({match[contact_keys[1]]})")
        choice = input("Contact number to delete(or cancel): ")
        if choice.lower() == "0":
            print("Operation cancelled.Returning to the main menu...")
            return
        if int(choice) < 1 or int(choice) > len(matches):
            print("ERROR: Invalid choice.")
            return
    contact = matches[int(choice) - 1]

    #Confirmation section for deletion the contact
    confirm = input(f"Are you sure you want to delete '{contact['name']}'? (yes/no)(or 'cancel'): ")
    if confirm.lower() == "cancel":
        print("Deletion cancelled.Returning to the main menu...")
        return
    if confirm.lower() == "yes":
        contacts.remove(contact)
        print(f"Contact '{contact[contact_keys[0]]}'has been  deleted successfully.")
        return
    elif confirm.lower() == "no":
        print("Deletion cancelled.")
        return
    else:
        print("ERROR: Invalid choice.")
        return
def run_manager(contacts):
    '''The tuple key structure of contact record'''
    contact_keys = ('name', 'phone', 'email', 'country')

    #Main menu and loop for the Contact Manager."""
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search & Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        print("------------------------")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact(contacts,contact_keys)
        elif choice == "2":
            view_contacts(contacts,contact_keys)
        elif choice == "3":
            edit_contact(contacts,contact_keys)
        elif choice == "4":
            delete_contact(contacts,contact_keys)
        elif choice == "5":
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 5.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        try:
            sys.stdin = open(input_file_path, 'r')
        except FileNotFoundError:
            sys.exit(1)

    contacts_list = []
    run_manager(contacts_list)

    if len(sys.argv) > 1:
        sys.stdin.close()










