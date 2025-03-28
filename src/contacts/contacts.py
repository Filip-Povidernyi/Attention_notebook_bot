from src.utils.common import print_help
from .classes.contacts_book import ContactsBook
from src.contacts.handler import handlers
from .birthdays import get_upcoming_birthdays
from ..utils.decorators import auto_save_on_error
from ..utils.autocomplete import suggest_command


"""
Module for managing contacts in the application.

This module provides functionality to interact with and manage contacts.
It includes a command-line interface (CLI) for performing actions with contacts.
"""


@auto_save_on_error
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
        "edit":         "Edit contact name, phone, etc.",
        "find":         "Find a contacts by query",
        "birthdays":    "Show upcoming birthdays",
        "help":         "Show this help",
        "back":         "Go back to the main menu"
    }

    print("\n\nYou are in Address Book now")
    print_help(commands)

    while True:

        cmd = input(
            "\nEnter a command (or 'help' for available commands): ").strip().lower()

        match cmd:
            case "add":
                result = handlers["add"](book)
                if result:
                    print(result)
                else:
                    continue

            case "delete":
                print(handlers["delete"](book))

            case "show-all":
                handlers["show-all"](book)

            case "edit":
                print(handlers["edit"](book))

            case "birthdays":
                get_upcoming_birthdays()

            case "find":
                found_contacts = handlers["find"](book)

                if found_contacts:
                    for contact in found_contacts:
                        print(contact)
                elif found_contacts is None:
                    print("You back to menu.")
                    print_help({
                        "1":    "Go to Address Book",
                        "2":    "Go to your Notes",
                        "help": "Show this help",
                        "exit": "Exit the application"
                    })
                else:
                    print("No contacts found.")

            case "help":
                print_help(commands)

            case "back":
                print("\nGoing back to the main menu...")
                print_help({
                    "1":    "Go to Address Book",
                    "2":    "Go to your Notes",
                    "help": "Show this help",
                    "exit": "Exit the application"
                })
                break
            case _:
                suggested = suggest_command(cmd, list(commands.keys()), 0.5)
                if suggested:
                    print(
                        f"Unknown command '{cmd}'.\nMaybe you mean '{suggested}'?")

                else:
                    print(f"Unknown command '{cmd}'. Please try again.")
