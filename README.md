# Use and Instructions to run these projects
These all projects are developed by python, So there is a need of installation of python to run these projects.And also all these projects are only terminal version and tested on IDE.
# Article Analyzer

A simple Django web app that analyzes an article's word frequency. It takes user input, counts how many times each word appears, and displays the sorted results.

## Features

- Accepts user-submitted article text
- Counts total words
- Shows how often each word appears
- Displays results sorted by frequency

## How to Run

1. Clone the repository
2. Make sure Django is installed:
3. Run the server: python manage.py runserver
4. Open your browser and go to: http://127.0.0.1:8000/

## File Overview

- `views.py`: Contains logic to analyze the article
- `Artical_analyzer.html`: Input form for users
- `2nd_analyzer.html`: Displays results



> 💡 Note: Make sure your Django templates are set up correctly in `settings.py`.
---

# Zombie Game Simulation

A simple Python-based simulation using Object-Oriented Programming (OOP), featuring a player and zombie-like enemies with health, lives, and attack mechanics.

## 👾 Game Features

- `Enemy` class with hit points and lives
- `Brain_eater`: can randomly dodge attacks
- `king_Brain_eater`: stronger enemy with reduced damage taken
- `Player`: has lives, levels, and score system
- Demonstrates encapsulation, inheritance, and polymorphism

## 🕹️ How to Play

The game is run in the terminal. A loop attacks the `king_Brain_eater` until all lives are lost.

### Run the Game:

python main.py
## Concepts Used
OOP Principles (Encapsulation, Inheritance, Polymorphism)

Randomization (enemy ducking logic)

Time measurement using time module

Private attributes and property setters/getters

📂 File Structure
bash
Copy
Edit
zombie_game/
├── enemy_zombie.py     # Enemy and Brain_eater classes
├── player_zombie.py    # Player class
└── main.py             # Game runner script
📌 Requirements
Python 3.x
No external libraries required.

Made with 💻 and ☕ by Anas Obaid 
---
# 💳 Digital Banking System (Python CLI)

A simple command-line based digital bank simulation using Python.  
Supports account creation, login, deposits, withdrawals, balance checking, and transaction history — all stored in text files.

---

## 🚀 Features

- 🔐 Secure login with username and password
- 💰 Deposit and withdraw funds
- 📊 View current balance
- 📋 Transaction history with date and time
- 📁 File-based storage (each account has a `.txt` file)

---

## 🛠️ How It Works

- User credentials and transactions are saved in a text file (`<username>.txt`)
- Deposits and withdrawals update the file and maintain history
- Input is validated with custom prompts
- ANSI colors used for user-friendly output

---

## ▶️ How to Run


python bank.py
Replace bank.py with your actual filename.

📂 Project Structure
bash
Copy
Edit
digital_bank/
└── bank.py              # Main file containing all functionality
🧪 Example
text
Copy
Edit
🏦 This is a Digital bank.
For login press 1
If you do not have account, press 2 for sign up
On login, users can:

Check balance (Press 1)

Deposit money (Press 2)

Withdraw money (Press 3)

View transaction history (Press 4)

✅ Requirements
Python 3.x
No external libraries needed.

Made with 💻 by Anas Obaid

---

# BMI Calculator – Python Project
This is a simple BMI (Body Mass Index) calculator written in Python. It allows users to input their weight (in kilograms) and height (in meters), and then calculates the BMI to determine the health category of the individual.

## Features
Accepts user input for weight and height

Calculates BMI using the standard formula

Provides health advice based on BMI value

## Categorizes BMI as:

Underweight

Healthy

Overweight

Obese
 
## Sample Output

This is BMI software
Enter weight in kg : 70
Enter height in meters : 1.75
healthy
Good! You have to hold this health.
## How to Run
💡 You need Python 3 installed on your system.

Save the code in a file named bmi_calculator.py

Open a terminal and navigate to the file location

Run the script with:

python bmi_calculator.py
🛠️ Technologies Used
Python 3

## 📌 Future Improvements (Optional)
GUI version using Tkinter or PyQt

Store BMI records for multiple users

Add unit conversion (lbs/ft to kg/m

## 📄 License
This project is open-source and free to use under the MIT License.

# 🎯 Number Guessing Game – Python Project
This is a beginner-friendly Number Guessing Game built using Python. The program generates a random number between 1 and 10, and the user has a total of 5 attempts to guess it correctly.

## 🚀 Features
Generates a random number between 1 and 10 each round

Accepts user input for guessing

Informs the user if the guess was correct or not

Allows up to 5 attempts

Gives motivational messages after each round

## 🧠 How It Works
The program starts a loop with 5 attempts.

On each attempt:

A random number (1–10) is generated.

The user guesses a number.

The program compares both numbers and outputs the result.

The game continues until all 5 attempts are used.

## 🖥️ Sample Output

Guess number between 1 to 10: 7
Computer thinked: 3
you lost this turn
make another one try

Guess number between 1 to 10: 5
Computer thinked: 5
Nice! you won the game
you guessed correct
## 🔧 How to Run
💡 Make sure Python 3 is installed on your system.

Save the code as number_guessing_game.py

Open terminal/command prompt

Run the file:
python number_guessing_game.py
🛠️ Technologies Used
Python 3

random module

## 📌 Possible Enhancements
Keep track of total score or correct guesses

Add difficulty levels (e.g., Easy: 1–10, Hard: 1–50)

GUI version using Tkinter

Multiplayer mode

## 📄 License
This project is licensed under the MIT License.
### This game is developed by ANAS.

# ✅ To-Do List CLI – Python Project
A simple yet functional command-line to-do list built in Python. It allows users to add, view, remove, and mark tasks as done. Task data is saved persistently in a tasks.txt file in the working directory.

## 🚀 Features
📄 View existing tasks

➕ Add new tasks

❌ Remove a task by its number

✅ Mark any task as done

📁 Tasks are saved to a local tasks.txt file

🔁 User-friendly looped menu for continuous use

📂 Data Format
Tasks are stored in the following format in tasks.txt:

1|[ ]|Buy groceries
2|[ ]|Finish homework
3|✅|Go for a walk
### Each line contains:

Task number

Status ([ ] for pending, ✅ for done)

Task description
## Sample Output

===To-do-list===
1.To view tasks list
2.To add a new task
3.To remove a task
4.To mark a task as done

Enter your choice:
2
==ADD TASK===
Enter task name that you want to add: Buy milk
1|[ ]|Buy milk
## 🧠 How to Use
✅ Prerequisites: Python 3 installed

Save the script as todo.py

Open a terminal in the same directory

Run the script with:
python todo.py
Interact with the menu by entering numbers (1–4) to perform actions

## Technologies Used
Python 3

Standard library modules:

os

input(), try-except, and file I/O

## 📌 Possible Enhancements
Add a due date field for each task

Add task priority system (low, medium, high)

Export tasks to CSV or JSON

Build GUI version using Tkinter

Create a web app version using Flask/Django

## 📄 License
This project is licensed under the MIT License.





























































