# Midterm-project-Python-
⚾ Baseball Team Manager
Overview

The Baseball Team Manager is a Python-based console application designed to manage a baseball team lineup efficiently. The program allows users to add, remove, edit, and rearrange players while automatically calculating batting averages. Player data is stored in a CSV file to ensure persistence between program runs.

This project demonstrates object-oriented programming principles, modular design, structured file handling, and input validation.

Project Structure
Baseball-Team-Manager/
├── main.py        # Application entry point and control logic
├── ui.py          # User interface and input/output handling
├── objects.py     # Player and Lineup class definitions
├── db.py          # CSV data management
├── players.csv    # Data storage file
└── README.md
Key Features

Display current lineup with formatted statistics

Add new players to the lineup

Remove players from the lineup

Reorder players within the lineup

Edit player position and statistics

Automatic batting average calculation (formatted to three decimals)

CSV-based data persistence

Input validation and error handling

Technical Implementation

The application follows a modular architecture:

objects.py contains the core business logic using Player and Lineup classes.

ui.py manages all user interaction and formatting.

db.py handles reading from and writing to the CSV file.

main.py coordinates program flow and integrates all components.

This separation of concerns ensures maintainability, clarity, and scalability.

How to Run

Ensure Python 3 is installed.

Navigate to the project directory.

Run the program:

python main.py
Author

Yadveer Kaur
