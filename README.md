# Personal Assistant

<p align="center">
  <img align="center" src="./assets/thumbnail.webp" width="300" title="Project thumbnail" alt="project thumbnail">
</p>

## Overview

Personal Assistant is a command-line application designed to help users manage their contacts and notes efficiently. It allows storing, searching, editing, and deleting contact details and notes while ensuring data integrity and easy access.

## Features

### Contact Management

- Add new contacts with names, addresses, phone numbers, emails, and birthdays.
- Search contacts by name, phone number, or other details.
- Edit and delete contacts.
- Display a list of contacts with upcoming birthdays within a specified number of days.
- Validate phone numbers and email addresses upon input.

### Notes Management

- Add, edit, delete, and search for notes.
- Assign tags to notes for easy categorization.
- Search and sort notes by tags.

### Data Storage

- All data (contacts, notes) is stored persistently on the user's local drive.
- The application can be restarted without data loss.

### Intelligent Assistance

- The assistant attempts to analyze user input and suggest the most relevant command based on context.

## Installation

local:
`bash pip install . `

start:
`bash f4-notebook `

### Requirements

- Python 3.12+

### Setup Instructions

1. Clone the Repository:

   ```bash
   git clone https://github.com/Filip-Povidernyi/Attention_notebook_bot.git
   ```

2. Navigate to the Project Directory:

   ```bash
   cd personal-assistant
   ```

3. Set Up a Virtual Environment:

   - For Windows:
     ```bash
     python -m venv .venv
     .\.venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

4. Install Dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Run the Application:

   ```bash
   python bot-code/main.py
   ```

## Build Docker image

Execute the following command in the project root directory to build the Docker image:

```bash
docker build -t icxodnik988/f4-notebook .
```

Then deploy the image to the dockerhub repository:

> [!NOTE] You need to be logged in to push the image to the repository.

```bash
docker push icxodnik988/f4-notebook
```

### Usage

### Docker

> [!NOTE] This is a alternative to install the package as an application using pip.
> To run the application using Docker, you need to have Docker installed on your machine.
> Just run the image from the public dockerhub repository:

```bash
docker run -it -v f4-notebook:/app/db icxodnik988/f4-notebook
```

## Available Commands

### MAIN MENU COMMANDS

- `contacts (1)`: "Go to Contacts Book",
- `notes    (2)`: "Go to your Notes",
- `vnotes   (3)`: "Go to your Notes (UI)",
- `help     (4)`: "Show this help",
- `exit     (0)`: "Exit the application"

### CONTACT MENU COMMANDS

- `add       (1)`: "Add a new contact",
- `delete    (2)`: "Delete a contact",
- `show-all  (3)`: "Show all contacts",
- `edit      (4)`: "Edit contact name, phone, etc.",
- `find      (5)`: "Find a contact",
- `birthdays (6)`: "Show upcoming birthdays",
- `help      (7)`: "Show this help",
- `back      (0)`: "Go back to the main menu"

### NOTE MENU COMMANDS

- `add          (1)`: "Add a new note (add <name>)",
- `view         (2)`: "View a note (view <name>)",
- `search       (3)`: "Search for a notes (search <term>)",
- `edit         (4)`: "Edit a note (edit <name>)",
- `delete       (5)`: "Delete a note (delete <name>)",
- `add_tag      (6)`: "Add a tag to a note",
- `remove_tag   (7)`: "Remove a tag from a note",
- `view_tags    (8)`: "View tags of a note",
- `search_tag   (9)`: "Search notes by tag (search_tag <tag>)",
- `sort_by_tags (10)`: "Sort notes by number of tags",
- `help         (11)`: "Show this help",
- `back         (0)`: "Go back to the main menu"

### Notes

- Use the `help` command to view details about command usage.
- Ensure that the `requirements.txt` file is up to date.
- Keep your Python version compatible with the specified requirements to avoid issues.

## Contribution

Contributions are welcome! If you'd like to improve the project, feel free to fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the [MIT License](./LICENSE).
