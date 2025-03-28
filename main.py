import atexit
from src.utils.common import print_help
from src.persistence.storage import load_data, save_data
from src.contacts.contacts import contacts_main
from src.notes.notes import notes_main
from src.utils.decorators import auto_save_on_error
from src.utils.autocomplete import suggest_command
from rich.console import Console


console = Console()


@auto_save_on_error
def main():
    """
    Main entry point for the Personal Assistant application.

    This script runs the main loop, allowing users to interact with the app.
    """

    commands = {
        "1":    "Go to Address Book",
        "2":    "Go to your Notes",
        "help": "Show this help",
        "exit": "Exit the application"
    }

    console.print("\nWelcome to your Personal Assistant!", style="steel_blue")
    console.print("How can I assist you today?\n", style="steel_blue")
    print_help(commands)

    book, notes = load_data()

    # Saves user's data upon normal interpreter termination
    atexit.register(save_data, book, notes)

    while True:

        cmd = input(
            "\nEnter a command (or 'help' for available commands): ").strip().lower()

        match cmd:
            case "1":
                contacts_main(book)

            case "2":
                notes_main(notes)

            case "help":
                print_help(commands)

            case "exit":
                print("Goodbye, have a nice day!")
                break
            case _:

                suggested = suggest_command(cmd, list(commands.keys()), 0.5)
                if suggested:
                    console.print(
                        f"Unknown command '{cmd}'.\nMaybe you mean '{suggested}'?", style="deep_pink4")

                else:
                    console.print(
                        f"Unknown command '{cmd}'. Please try again.", style="deep_pink4")


if __name__ == "__main__":
    main()
