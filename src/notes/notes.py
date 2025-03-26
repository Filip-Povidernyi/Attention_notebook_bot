from .classes.note_book import Notebook

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


    notebook = Notebook()

    while True:
        cmd = input("Enter a command: ").strip().lower()

        match cmd:
            case "add":
                addNote(notebook)
            case "search":
                searchNotes(notebook)
            case "edit":
                editNote(notebook)
            case "delete":
                deleteNote(notebook)
            case "test":
                print("This is a test stub message to check the notes function.")
            case "exit" | "close":
                break
            case _:
                print("Unknown command. Please try again.")
            

def addNote(notebook: Notebook):
    name = input("Enter note name: ").strip()
    content = input("Enter note content: ")

    notebook.addNote(name, content)

def searchNotes(notebook: Notebook):
    pass

def editNote(notebook: Notebook):
    pass

def deleteNote(notebook: Notebook):
    pass


