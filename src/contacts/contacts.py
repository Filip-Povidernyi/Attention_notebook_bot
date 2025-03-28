from src.utils.common import print_help
from .classes.contacts_book import ContactsBook
from src.contacts.handler import handlers
from .birthdays import get_upcoming_birthdays
from ..utils.decorators import auto_save_on_error
from ..utils.autocomplete import suggest_command
from src.utils.constants import MAIN_MENU_COMMANDS, CONTACT_MENU_COMMANDS


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


    print("\n\nYou are in Address Book now")
    print_help(CONTACT_MENU_COMMANDS)

    while True:

        cmd = input(
            "\nEnter a command (or 'help' for available commands): ").strip().lower()

        match cmd:
            case "add" | "a":
                result = handlers["add"](book)
                if result:
                    print(result)
                else:
                    continue

            case "delete" | "d":
                print(handlers["delete"](book))

            case "show-all" | "sh":
                handlers["show-all"](book)

            case "edit" | "e":
                print(handlers["edit"](book))

            case "birthdays" | "b":
                get_upcoming_birthdays()

            case "find" | "f":
                found_contacts = handlers["find"](book)

                if found_contacts:
                    for contact in found_contacts:
                        print(contact)
                elif found_contacts is None:
                    print("You back to menu.")
                    print_help(MAIN_MENU_COMMANDS)
                else:
                    print("No contacts found.")

            case "help" | "h":
                print_help(CONTACT_MENU_COMMANDS)

            case "back" | "b":
                print("\nGoing back to the main menu...")
                print_help(MAIN_MENU_COMMANDS)
                break
            case _:
                suggested = suggest_command(cmd, list(CONTACT_MENU_COMMANDS.keys()), 0.5)
                if suggested:
                    print(
                        f"Unknown command '{cmd}'.\nMaybe you mean '{suggested}'?")

                else:
                    print(f"Unknown command '{cmd}'. Please try again.")
