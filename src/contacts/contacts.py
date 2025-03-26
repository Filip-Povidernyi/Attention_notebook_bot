from .classes.contacts_book import ContactsBook
from .handler import add_contact


def contacts_main(book: ContactsBook):
    """
    Main loop for managing contacts in the address book.

    This function creates an instance of AddressBook and enters a loop where it waits for user 
    input to perform actions.
    """

    print("\n\nYou are in Address Book now\n")
    print('To Add New Contact, enter "add"')
    print('\nTo go to the main menu, enter "exit" or "close"\n')

    while True:

        cmd = input("Enter a command: ").strip().lower()

        if cmd == "add":
            result = add_contact(book)
            if result:
                print(result)
            else:
                continue

        elif cmd in ("exit", "close"):
            break

        else:
            print("Unknown command. Please try again.")
