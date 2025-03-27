import atexit
from src.utils.common import print_help
from src.persistence.storage import load_data, save_data
from src.contacts.contacts import contacts_main
from src.notes.notes import notes_main
from src.utils.decorators import auto_save_on_error


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

    print("\nWelcome to your Personal Assistant!")
    print("How can I assist you today?")
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
                print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
