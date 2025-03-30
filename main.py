from src.utils.password import prompt_password
from src.utils.constants import MAIN_MENU_COMMANDS
from rich.console import Console
from src.utils.autocomplete import suggest_command
from src.utils.decorators import auto_save_on_error
from src.notes.notes_ui import notes_main as notes_main_ui
from src.notes.notes import notes_main
from src.contacts.contacts import contacts_main
from src.persistence.storage import load_data, save_data
from src.utils.common import print_help
import atexit
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "src")))


console = Console()


@auto_save_on_error
def main():
    """
    Main entry point for the Personal Assistant application.

    This script runs the main loop, allowing users to interact with the app.
    """

    PASSWORD = prompt_password()

    book, notes = load_data(PASSWORD)

    while book is None or notes is None:
        console.print("❌ Try again with the correct password.",
                      style="deep_pink4")
        PASSWORD = prompt_password()
        book, notes = load_data(PASSWORD)

    # Saves user's data upon normal interpreter termination
    atexit.register(save_data, book, notes, PASSWORD)

    console.print("\nWelcome to your Personal Assistant!", style="steel_blue")
    console.print("How can I assist you today?\n", style="steel_blue")
    print_help(MAIN_MENU_COMMANDS)

    while True:

        cmd = input(
            "\nEnter a command (or 'help' (3) for available commands): ").strip().lower()

        if not cmd:
            console.print("Please enter a command from the list of available commands.",
                          style="deep_pink4")
            continue

        match cmd:
            case "contacts" | "1":
                contacts_main(book)

            case "notes" | "2":
                notes_main(notes)

            case "vnotes" | "3":
                notes_main_ui(notes)

            case "help" | "4":
                print_help(MAIN_MENU_COMMANDS)

            case "exit" | "0":
                exit_program()

            case _:

                suggested = suggest_command(
                    cmd, list(MAIN_MENU_COMMANDS.keys()), 0.5)
                if suggested:
                    console.print(
                        f"Unknown command '{cmd}'.\nMaybe you mean '{suggested}'?", style="deep_pink4")

                else:
                    console.print(
                        f"Unknown command '{cmd}'. Please try again.", style="deep_pink4")


def exit_program():
    console.print("Goodbye, have a nice day!", style="steel_blue")
    sys.exit(0)


if __name__ == "__main__":
    main()


# def book_note():
#     main()
