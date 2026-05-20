# Python-Project

# Python Mini Toolkit: My First Coding Project

## Project Description
The Python Mini Toolkit is a terminal-based application designed to provide users with utility tools to handle small, everyday tasks. Built as a portfolio pieces for the Life Choices program, this project demonstrates a fundamental understanding of core programming concepts, logical flow, data management, and code modularity. 

The application utilizes a clean, interactive menu layout that splits operations cleanly across a main driver module and a helper utilities module.

---

## Features
The toolkit consists of three interactive mini-tools chosen from the project framework:

1. **Guessing Game:** An interactive number game where the user gets 5 chances to guess a randomly generated number between 1 and 100, receiving hints if their guesses are too high or low.
2. **Budget Calculator:** A dynamic budgeting utility tailored for South African Rand (R) that accepts a user's monthly income, tracks an unlimited list of individual custom expenses using modern list structures, and outputs a complete breakdown of total expenses and remaining net savings.
3. **Grade Calculator:** A validation-safe grading utility that prompts users for a percentage test score between 0 and 100, evaluates it against standard ranges, and returns a final letter grade (A, B, C, D, or F).

---

## Python Concepts Used
To meet the requirements of the submission brief, this project integrates the following core programming methodologies:

* **Variables & Type Casting:** Handled distinct data types (`int` for guessing targets, `float` for currencies, `string` for inputs) and cast terminal inputs appropriately to run accurate calculations.
* **Control Flow (Conditionals):** Implemented multi-layered structural evaluations using `if`, `elif`, and `else` statements across all tools to direct traffic based on input benchmarks.
* **Loops & Loop Control:** Employed dynamic `while True` logic loops combined with custom loop breaks (`break`) to consistently process data entries, validate constraints, and keep the main menu active.
* **Data Structures (Lists):** Used dynamic, parallel lists (`expense_names` and `expense_amounts`) in the budgeting segment to store multiple descriptive data payloads on the fly.
* **Modularity (Functions & Modules):** Organized features systematically by isolating logic into standalone functions inside a custom module (`helpers.py`) and clean execution control inside `main.py`.
* **Error Handling:** Wrapped terminal numeric input sequences within functional `try-except` blocks to proactively handle `ValueError` disruptions and avoid program crashes.

---

## How to Run the Project

### Prerequisites
Make sure you have Python 3 installed on your local machine.

### Installation & Execution Steps
1. Clone this repository to your local system or download the source files.
2. Open your terminal, command prompt, or preferred code editor and navigate to the project directory:
   ```bash
   cd python-mini-toolkit
