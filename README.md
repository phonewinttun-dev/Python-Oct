# Python-Oct

Beginner-friendly Python examples covering conditional statements, loops, and a practical ATM banking system.

## Project Structure

```
Python-Oct/
├── Conditionals/
│   └── main.py
├── Loops/
│   ├── main.py
│   └── atm_system.py
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

### 3. Capstone Project: Simple ATM System (`Loops/atm_system.py`)
A practical CLI banking application demonstrating real-world usage of conditionals and loops:
- `while` loop with retry counter for secure PIN verification (max 3 attempts)
- `while True` for the interactive ATM operational menu
- `if`, `elif`, `else` for input validation and balance checks
- `for` loop with `enumerate()` for displaying formatted transaction history
- `break` and `continue` control flow

## Getting Started

Run the scripts using Python:

```bash
# Conditionals
python Conditionals/main.py

# Loops
python Loops/main.py

# ATM System (Default PIN: 1234)
python Loops/atm_system.py
```
