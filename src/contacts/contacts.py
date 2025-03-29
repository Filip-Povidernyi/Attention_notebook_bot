from src.utils.common import print_help
from .classes.contacts_book import ContactsBook
from src.contacts.handler import handlers
from .birthdays import get_upcoming_birthdays
from ..utils.decorators import auto_save_on_error
from ..utils.autocomplete import suggest_command
from rich.console import Console
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

    console = Console()
    console.print("\n\nYou are in Address Book now", style="steel_blue")
    print_help(CONTACT_MENU_COMMANDS)


    while True:

        cmd = input(
            "\nEnter a command (or 'help' (7) for available commands): ").strip().lower()
        
        if not cmd:
            console.print("Please enter a command from the list of available commands.", 
                          style="deep_pink4")
            continue

        match cmd:
            case "add" | "1":
                result = handlers["add"](book)
                if result:
                    console.print(f"{result}", style="green")
                else:
                    continue

            case "delete" | "2":
                console.print(f"{handlers["delete"](book)}", style="green")

            case "show-all" | "3":
                handlers["show-all"](book)

            case "edit" | "4":
                console.print(f"{handlers["edit"](book)}", style="green")

            case "find" | "5":
                found_contacts = handlers["find"](book)

                if found_contacts:

                    handlers["show-all"](found_contacts)

                elif found_contacts is None:
                  
                    print("You back to menu.")
                    print_help(MAIN_MENU_COMMANDS)
                else:
                    print("No contacts found.")

            case "birthdays" | "6":
                get_upcoming_birthdays(book)

            case "help" | "7":
                print_help(CONTACT_MENU_COMMANDS)

            case "back" | "8":
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
