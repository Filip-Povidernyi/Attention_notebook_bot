from .classes.contacts_book import ContactsBook
from .handler import add_contact, delete_contact, show_all
from ..utils.decorators import auto_save_on_error


@auto_save_on_error
def contacts_main(book: ContactsBook):
    """
    Main loop for managing contacts in the address book.

    This function creates an instance of AddressBook and enters a loop where it waits for user 
    input to perform actions.
    """

    print("\n\nYou are in Address Book now\n")
    print('To Add New Contact, enter "add"\n')
    print('To delete a contact, enter "delete"\n')
    print('\nTo go to the main menu, enter "exit" or "close"\n')

    while True:

        cmd = input("Enter a command: ").strip().lower()

        if cmd == "add":
            result = add_contact(book)
            if result:
                print(result)
            else:
                continue
        if cmd == "delete":
            print(delete_contact(book))

        if cmd == "show-all":
            show_all(book)

        elif cmd in ["exit", "close"]:
            break

        else:
            print("Unknown command. Please try again.")
