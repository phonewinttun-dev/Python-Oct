# Python-Oct

Beginner-friendly Python examples covering conditional statements, loops, functions, and practical CLI projects.

## Project Structure

```
Python-Oct/
├── Conditionals/
│   └── main.py
├── Loops/
│   ├── main.py
│   └── atm_system.py
├── Functions/
│   ├── main.py
│   └── student_grade_system.py
└── README.md
```

## Topics Covered

### 1. Conditionals (`Conditionals/main.py`)
- Basic `if` statement
- `if-else` statement
- `if-elif-else` ladder
- Logical operators (`and`, `or`, `not`)
- Membership operators (`in`, `not in`)
- Nested `if` statements

### 2. Loops (`Loops/main.py`)
- Basic `while` loop (Counters)
- `while` loop with `break` and `continue`
- `for` loop with `range()` (start, stop, step)
- `for` loop over Lists, Strings, and Dictionaries (`.items()`)
- `for` loop with `enumerate()`
- `for` loop with `break` and `continue`
- Nested loops (Grid/Matrix)

### 3. Functions (`Functions/main.py`)
- Basic function definition (`def`) and function invocation
- Functions with single and multiple parameters/arguments
- Default parameter values
- Returning values (`return` vs `print`)
- Returning boolean conditions
- Returning multiple values (tuple unpacking)

### 4. Capstone Project 1: Simple ATM System (`Loops/atm_system.py`)
A practical CLI banking application demonstrating real-world usage of conditionals and loops:
- `while` loop with retry counter for secure PIN verification (max 3 attempts)
- `while True` for the interactive ATM operational menu
- `if`, `elif`, `else` for input validation and balance checks
- `for` loop with `enumerate()` for displaying formatted transaction history
- `break` and `continue` control flow

### 5. Capstone Project 2: Student Grade System (`Functions/student_grade_system.py`)
A modular CLI grade management application demonstrating practical use of functions:
- Modular function design (`calculate_total`, `calculate_average`, `check_pass_all`, `determine_grade`, `display_report_card`)
- Functions with default arguments (`pass_mark=50`)
- Value returning functions and formatted output
- Interactive loop with student record tracking

## Getting Started

Run the scripts using Python:

```bash
# Conditionals
python Conditionals/main.py

# Loops
python Loops/main.py

# Functions
python Functions/main.py

# Student Grade System
python Functions/student_grade_system.py
```
