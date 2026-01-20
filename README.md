🚀 Elevator Control Logic

A simple OOP-based Python simulation of an elevator system that processes floor requests, simulates step-by-step movement, and calculates total time taken. The project demonstrates Object-Oriented Programming, modular design, input validation, and file handling.

📌 Key Features

-Takes maximum floor of the building from user

-Takes current elevator floor

-Accepts multiple floor requests

-Filters invalid and duplicate requests

-Moves elevator one floor at a time

-Calculates total time taken

-Logs elevator movement using file handling

📁 Project Structure

elevator_control/

├── app.py                # Main controller

├── elevator_engine.py    # Elevator movement logic (OOPS)

├── request_manager.py    # Request validation & sorting

├── input_handler.py      # User input handling

├── validator.py          # Floor validation

├── activity_logger.py    # File logging

└── README.md

▶️ How to Run

git clone https://github.com/dakshitaS4/elevator_control.git

cd elevator_control

python app.py


Make sure you run the command from the folder containing app.py.

🧪 Sample Output

Enter maximum floor of the building: 10

Enter current floor: 2

Enter floor requests separated by space: 5 6

Elevator Movement:

Reached floor 3

Reached floor 4

Reached floor 5

Reached floor 6

Total time taken: 4 units

🧠 OOPS Concepts Used

Encapsulation – Elevator state and behavior inside classes

Abstraction – Internal movement logic hidden from controller

Single Responsibility Principle – Each module has one clear task

