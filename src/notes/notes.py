"""
Module for managing notes in the application.

This module provides functionality to interact with and manage notes.
It includes a command-line interface (CLI) for performing actions such as 
displaying test messages and exiting the program.
"""

def notes_main():
    """
    Main loop for managing notes in the application.

    This function presents a simple interface to the user for interacting with the notes section 
    of the application. It provides options for displaying a test message and exiting the program.
    """
    
    print("\n\nYou are in Notes now\n")
    print('To see a test message, enter "test"')
    print('\nTo go to the main menu, enter "exit" or "close"\n')

    while True:

        cmd = input("Enter a command: ").strip().lower()

        if cmd == "test":
            print("This is a test stub message to check the notes function.")

        elif cmd in ("exit", "close"):
            break

        else:
            print("Unknown command. Please try again.")
