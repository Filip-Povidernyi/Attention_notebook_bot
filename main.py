import atexit
from src.utils.common import print_help
from src.persistence.storage import load_data, save_data
from src.contacts.contacts import contacts_main
from src.notes.notes import notes_main
from src.utils.decorators import auto_save_on_error
from src.utils.autocomplete import suggest_command
from src.utils.constants import MAIN_MENU_COMMANDS


@auto_save_on_error
def main():
    """
    Main entry point for the Personal Assistant application.

    This script runs the main loop, allowing users to interact with the app.
    """

    print("\nWelcome to your Personal Assistant!")
    print("How can I assist you today?")
    print_help(MAIN_MENU_COMMANDS)

    book, notes = load_data()

    # Saves user's data upon normal interpreter termination
    atexit.register(save_data, book, notes)

    while True:

        cmd = input(
            "\nEnter a command (or 'help' for available commands): ").strip().lower()

        match cmd:
            case "ad" | "1":
                contacts_main(book)

            case "note" | "2":
                notes_main(notes)

            case "help" | "3":
                print_help(MAIN_MENU_COMMANDS)

            case "exit" | "4":
                print("Goodbye, have a nice day!")
                break
            case _:

                suggested = suggest_command(cmd, list(MAIN_MENU_COMMANDS.keys()), 0.5)
                if suggested:
                    print(
                        f"Unknown command '{cmd}'.\nMaybe you mean '{suggested}'?")

                else:
                    print(f"Unknown command '{cmd}'. Please try again.")


if __name__ == "__main__":
    main()
