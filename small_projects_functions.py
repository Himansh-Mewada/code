def load_contacts(filename):
    """
    Loads contacts from a specified file.
    Assumes each contact is on a new line in the format: "Name PhoneNumber"
    Returns a list of contact dictionaries.
    """
    loaded_contacts = []
    try:
        with open(filename, "r") as file:
            for line in file:
                # Use .strip() to remove leading/trailing whitespace, including the newline character
                parts = line.strip().split(" ")
                if len(parts) >= 2: # Ensure there are at least two parts (name and number)
                    name = parts[0]
                    # Join the rest of the parts for numbers that might contain spaces
                    number = " ".join(parts[1:])
                    contact = {"name": name, "number": number}
                    loaded_contacts.append(contact)
                else:
                    print(f"Warning: Skipping malformed line in {filename}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Starting with an empty contact list.")
    except Exception as e:
        print(f"An unexpected error occurred while loading contacts from '{filename}': {e}")
    return loaded_contacts

def save_contacts(filename, contacts):
    """
    Saves a list of contact dictionaries to a specified file.
    Each contact is saved on a new line in the format: "Name PhoneNumber"
    """
    try:
        # Use 'w' mode to overwrite the file with the current list of contacts
        with open(filename, "w") as file:
            for contact in contacts:
                # Ensure the contact dictionary has 'name' and 'number' keys
                name = contact.get("name", "Unknown Name")
                number = contact.get("number", "Unknown Number")
                file.write(f"{name} {number}\n")
        print(f"Contacts successfully saved to '{filename}'.")
    except IOError as e:
        print(f"Error: Could not write to file '{filename}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while saving contacts to '{filename}': {e}")

