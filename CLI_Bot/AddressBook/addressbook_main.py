# from .addressbook_classes.addressbook_class import AddressBook # Не потрібен при використанні завантаження з файлу
from .handler import add_contact


def addressbook_main(book):

    print("Hello! How i can help you?")

    # book = AddressBook() # Не потрібен при використанні завантаження з файлу

    while True:

        cmd = input("Enter a command: ").strip().lower()

        if cmd == 'add':
            result = add_contact(book)
            if result:
                print(result)
            else:
                continue

        elif cmd == 'exit' or cmd == 'close':
            break

        else:
            print("Unknown command. Please try again.")
