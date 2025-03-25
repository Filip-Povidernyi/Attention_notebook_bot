from src.contacts.contacts import contacts_main
from src.notes.notes import notes_main

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

    while True:

        cmd = input("Enter a command: ").strip().lower()

        if cmd == "1":
            contacts_main()

        elif cmd == "2":
            notes_main()

        elif cmd in ("exit", "close"):
            print("Goodbye!")
            break

        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
