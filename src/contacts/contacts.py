from src.utils.common import print_help
from .classes.contacts_book import ContactsBook
from .handler import add_contact, delete_contact, show_all
from .birthdays import get_upcoming_birthdays

"""
Module for managing contacts in the application.

This module provides functionality to interact with and manage contacts.
It includes a command-line interface (CLI) for performing actions with contacts.
"""

def contacts_main(book: ContactsBook):
    """
    Main loop for managing contacts in the contacts book.

    This function uses an instance of ContactBook and enters a loop where it 
    waits for user input to perform actions.
    """

    commands = {
        "add":          "Add a new contact",
        "delete":       "Delete a contact",
        "show-all":     "Show all contacts",
        "birthdays":    "Show upcoming birthdays",
        "help":         "Show this help",
        "back":         "Go back to the main menu"
    }

    print("\n\nYou are in Address Book now")
    print_help(commands)
    
    while True:

        cmd = input("\nEnter a command (or 'help' for available commands): ").strip().lower()

        match cmd:
            case "add":
                result = add_contact(book)
                if result:
                    print(result)
                else:
                    continue
            case "delete":
                print(delete_contact(book))
            case "show-all":
                show_all(book)
            case "birthdays":
                get_upcoming_birthdays()
            case "help":
                print_help(commands)
            case "back":
                break
            case _:
                print("Unknown command. Please try again.")
