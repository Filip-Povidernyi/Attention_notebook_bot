import atexit
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
    
    print("\nWelcome to your Personal Assistant!")
    print("How can I assist you today?\n")
    print('To enter the Address Book, enter "1"')
    print('To enter Your Notes, enter "2"')
    print('\nTo exit, enter "exit" or "close"\n')

    book, notes = load_data()

    # Додав для автоматичного збереження перед виходом (говорив про дану бібліотеку на першому зідзвоні)
    atexit.register(save_data, book, notes)

    while True:

        cmd = input("Enter a command: ").strip().lower()

        if cmd == "1":
            contacts_main(book)

        elif cmd == "2":
            notes_main(notes)

        elif cmd in ("exit", "close"):
            print("Goodbye!")
            break

        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
