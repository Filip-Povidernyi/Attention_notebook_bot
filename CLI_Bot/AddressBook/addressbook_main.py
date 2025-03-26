from .addressbook_classes.addressbook_class import AddressBook
from .handler import add_contact
from src.contacts.birthdays import get_upcoming_birthdays


def addressbook_main():

    print("Hello! How i can help you?")

    book = AddressBook()

    while True:

        cmd = input("Enter a command: ").strip().lower()

        if cmd == 'add':
            result = add_contact(book)
            if result:
                print(result)
            else:
                continue

        elif cmd == "birthdays":
            result = get_upcoming_birthdays()

        elif cmd == 'exit' or cmd == 'close':
            break

        else:
            print("Unknown command. Please try again.")
