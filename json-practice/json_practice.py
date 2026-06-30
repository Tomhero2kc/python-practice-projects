import json
from pathlib import Path


CONTACTS_FILE = Path(__file__).parent / "contacts.json"


def load_contacts():
    try:
        with CONTACTS_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("The contacts file was not found. A new one will be created.")
        return []

    except json.JSONDecodeError:
        print("The contacts file contains invalid information.")
        return []


def save_contacts(contacts):
    with CONTACTS_FILE.open("w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)


def display_contacts(contacts):
    if not contacts:
        print("\nThere are no contacts to display.")
        return

    print("\nSaved Contacts")
    print("-" * 40)

    for number, contact in enumerate(contacts, start=1):
        print(f"{number}. {contact['name']}")
        print(f"   Email: {contact['email']}")
        print(f"   Phone: {contact['phone']}")


def add_contact(contacts):
    print("\nAdd a New Contact")

    name = input("Name: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone number: ").strip()

    if not name or not email or not phone:
        print("Please complete all the fields.")
        return

    new_contact = {
        "name": name,
        "email": email,
        "phone": phone
    }

    contacts.append(new_contact)
    save_contacts(contacts)

    print(f"{name} has been saved successfully.")


def main():
    print("Simple Contact List")

    contacts = load_contacts()
    display_contacts(contacts)

    choice = input(
        "\nDo you want to add a new contact? (yes/no): "
    ).strip().lower()

    if choice in ["yes", "y"]:
        add_contact(contacts)
        display_contacts(contacts)
    else:
        print("Okay, no contact was added.")


if __name__ == "__main__":
    main()