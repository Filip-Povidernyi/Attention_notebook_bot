# Personal Assistant

<p align="center">
  <img align="center" src="./assets/thumbnail.webp" width="300" title="Project thumbnail" alt="project thumbnail">
</p>


## Overview

Personal Assistant is a command-line application designed to help users manage their contacts and notes efficiently. It allows storing, searching, editing, and deleting contact details and notes while ensuring data integrity and easy access.

## Features

### Contact Management

* Add new contacts with names, addresses, phone numbers, emails, and birthdays.
* Search contacts by name, phone number, or other details.
* Edit and delete contacts.
* Display a list of contacts with upcoming birthdays within a specified number of days.
* Validate phone numbers and email addresses upon input.

### Notes Management

* Add, edit, delete, and search for notes.
* Assign tags to notes for easy categorization.
* Search and sort notes by tags.

### Data Storage

* All data (contacts, notes) is stored persistently on the user's local drive.
* The application can be restarted without data loss.

### Intelligent Assistance

* The assistant attempts to analyze user input and suggest the most relevant command based on context.

## Installation
local:
pip install .

start:
f4-notebook
### Requirements

* Python 3.7+

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
    * For Windows:
        ```bash
        python -m venv .venv
        .\.venv\Scripts\activate
        ```
    * For macOS/Linux:
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
    python main.py
    ```

#### Build Docker image

Execute the following command in the project root directory to build the Docker image:
```bash
docker build -t icxodnik988/f4-notebook .
```

Then deploy the image to the dockerhub repository:
> [!NOTE] You need to be logged in to push the image to the repository.
```bash
docker push icxodnik988/f4-notebook
```


## Usage

### Docker

> [!NOTE] This is a alternative to install the package as an application using pip.
To run the application using Docker, you need to have Docker installed on your machine.
Just run the image from the public dockerhub repository:
```bash
docker run -it -v f4-notebook:/app/db icxodnik988/f4-notebook
```

### Available Commands

* `add-contact` — Add a new contact.
* `show-contact` — Display a contact by name.
* `search-contacts` — Search contacts by name, phone number, or email.
* `edit-contact` — Edit an existing contact.
* `delete-contact` — Delete a contact.
* `show-all-contacts` — Display all contacts.
* `birthday-in-days N` — Show contacts with upcoming birthdays in the next N days.
* `add-note` — Add a new note.
* `show-notes` — Display all notes.
* `search-notes` — Search notes by title, content, or tags.
* `edit-note` — Edit a note.
* `delete-note` — Delete a note.
* `sort-notes` — Sort notes by tag length.
* `exit` — Exit the application.
* `help` — Show available commands.

### Notes

* Use the `help` command to view details about command usage.
* Ensure that the `requirements.txt` file is up to date.
* Keep your Python version compatible with the specified requirements to avoid issues.

## Contribution

Contributions are welcome! If you'd like to improve the project, feel free to fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the [MIT License](./LICENSE).