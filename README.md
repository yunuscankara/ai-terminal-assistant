AI Terminal Assistant

A Python-based terminal assistant that combines REST API operations, local JSON memory, and a locally running Large Language Model (LLM) using Ollama.

This project was built as a hands-on learning project to practice Python programming, API integration, data persistence, error handling, and local AI integration.

Features

REST API Integration

* Retrieve and display users from a REST API.
* Search for users by ID.
* Display user information and email addresses.
* Send requests to add, update, and delete users.
* Handle API request errors.

Local Memory

* Store notes in a local JSON file.
* Add new notes.
* Display saved notes.
* Delete selected notes.
* Handle missing or invalid memory files.

Local AI Chat

* Integrate with a locally running LLM through Ollama.
* Use the Qwen2.5 3B model.
* Maintain conversation history during the current program session.
* Provide a continuous chat experience.
* Use a system instruction to encourage Turkish responses.
* Handle connection errors.

Command-Line Interface

* Interactive terminal menu.
* Command-based navigation.
* Input validation for supported operations.
* Help command for available features.

Technologies

* Python
* REST APIs
* Requests
* JSON
* Ollama
* Qwen2.5 3B
* Git and GitHub

Requirements

* Python 3
* pip
* Ollama
* The qwen2.5:3b model
* An internet connection for the external REST API features

Installation

1. Clone the repository

git clone https://github.com/yunuscankara/ai-terminal-assistant.git
cd ai-terminal-assistant

2. Install the Python dependency

python3 -m pip install requests

3. Install and prepare Ollama

Install Ollama, then download the model:

ollama pull qwen2.5:3b

Make sure Ollama is running before using the AI chat feature.

4. Run the application

python3 main.py

Available Commands

Command	Description
users	Retrieve and display users
user	Search for and display a user
email	Display email information
add	Send a request to add a user
update	Send a request to update a user
delete	Send a request to delete a user
remember	Save a note to local memory
memory	Display saved notes
forget	Delete a saved note
chat	Start a conversation with the local AI model
help	Display available commands
q	Exit the current interaction or application, depending on context

Follow the prompts displayed in the terminal when using each command.

Project Structure

ai-terminal-assistant/
├── main.py
├── memory.json
├── .gitignore
└── README.md

* main.py: Application logic, API operations, memory management, and AI chat.
* memory.json: Local storage for saved notes.
* .gitignore: Files and directories excluded from Git.
* README.md: Project documentation.

Important Notes

* The AI chat feature communicates with Ollama running locally on the machine.
* Conversation history is maintained in memory while the application is running. It is not automatically saved as a permanent chat history.
* Notes stored in memory.json persist between application sessions.
* The external REST API is intended for demonstration and testing. Successful write requests may not permanently change the API’s underlying data.
* AI responses may vary depending on the model and prompt.

Learning Objectives

This project helped me practice:

* Structuring a Python application with separate functions.
* Working with HTTP requests and REST APIs.
* Handling exceptions and invalid input.
* Reading and writing JSON files.
* Implementing basic local data persistence.
* Integrating a local LLM into a Python application.
* Managing conversation history.
* Documenting and maintaining a GitHub project.

Future Improvements

* Add automated tests.
* Improve input validation and error handling.
* Add more robust memory management.
* Refine AI response handling.
* Improve the overall application structure.