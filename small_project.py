import small_projects_functions
import os # Import the os module to check for file existence

# Global list to store contacts in memory
# Initialize by attempting to load from a default file
CONTACTS_FILE = "my_contacts.txt"
contact_list = [] # Initialize as empty list

# --- Initial Load ---
print("--- Contact Manager ---")
print("Loading contacts from 'my_contacts.txt'...")
contact_list = small_projects_functions.load_contacts(CONTACTS_FILE)
if not contact_list:
    print("No existing contacts found or file was empty. Starting with an empty list.")
else:
    print(f"Successfully loaded {len(contact_list)} contacts.")

# --- Helper Functions for Main App ---
def add_contact():
    """Prompts user for contact name and number and adds it to contact_list."""
    name = input("Enter contact name: ").strip()
    number = input("Enter contact number: ").strip()
    if name and number: # Ensure inputs are not empty
        contact = {"name": name, "number": number}
        contact_list.append(contact)
        print(f"Contact '{name}' added.")
    else:
        print("Name and number cannot be empty. Contact not added.")

def view_contacts():
    """Displays all contacts currently in contact_list."""
    if not contact_list:
        print("No contacts to display.")
        return
    print("\n--- Your Contacts ---")
    for index, contact in enumerate(contact_list):
        print(f"{index + 1}. Name: {contact.get('name', 'N/A')}, Phone: {contact.get('number', 'N/A')}")
    print("---------------------\n")

def search_contact():
    """Searches for a contact by name and displays their number."""
    search_name = input("Please enter the name of the person you want to look for: ").strip()
    found = False
    for contact in contact_list:
        if contact.get("name", "").lower() == search_name.lower(): # Case-insensitive search
            print(f"Contact found! Name: {contact['name']}, Phone: {contact['number']}")
            found = True
            break # Exit loop once found
    if not found:
        print(f"No contact found with the name '{search_name}'.")

def save_current_contacts():
    """Saves the current contact_list to the default file."""
    small_projects_functions.save_contacts(CONTACTS_FILE, contact_list)

# --- Main Application Loop ---
def main():
    """Main function to run the Contact Manager application."""
    print("\nIf you wish to import/export contacts, the current format is: 'Name PhoneNumber'")
    print("Example: Alice 123-32423-23")
    print("You don't need to enclose filenames in quotes when typing them, Python will handle it.")

    while True:
        print("\n--- Menu ---")
        print("1. Load contacts from a file")
        print("2. Save current contacts to a file")
        print("3. Add a new contact")
        print("4. View all contacts")
        print("5. Search for a contact by name")
        print("6. Quit")
        print("------------")

        choice = input("Enter your selected option: ").strip()

        if choice == '1':
            filename = input(f"Enter the filename to load from (e.g., '{CONTACTS_FILE}'): ").strip()
            # If the user just presses enter, use the default file
            if not filename:
                filename = CONTACTS_FILE
            
            # Load contacts and replace current list
            global contact_list
            contact_list = small_projects_functions.load_contacts(filename)
            print(f"Loaded {len(contact_list)} contacts from '{filename}'.")

        elif choice == '2':
            filename = input(f"Enter the filename to save to (e.g., '{CONTACTS_FILE}'): ").strip()
            # If the user just presses enter, use the default file
            if not filename:
                filename = CONTACTS_FILE
            
            small_projects_functions.save_contacts(filename, contact_list)

        elif choice == '3':
            add_contact()

        elif choice == '4':
            view_contacts()

        elif choice == '5':
            search_contact()

        elif choice == '6':
            print("Saving contacts before quitting...")
            save_current_contacts() # Save before exiting
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from the menu.")

# Run the main application
if __name__ == "__main__":
    main()




