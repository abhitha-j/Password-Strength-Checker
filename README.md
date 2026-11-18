# Password Strength Checker

A Python-based Password Strength Checker that evaluates passwords using predefined security rules and provides suggestions for improving password strength.

## Features

- Checks minimum password length.
- Detects uppercase and lowercase letters.
- Checks for numeric digits.
- Detects special characters.
- Rejects passwords containing spaces.
- Identifies a small list of commonly used passwords.
- Calculates a password strength score.
- Classifies passwords as Weak, Moderate, or Strong.
- Provides suggestions for improving password strength.
- Allows users to check multiple passwords.

## Technologies Used

- Python 3
- VS Code

## Concepts Practiced

- Functions
- Conditional statements
- Loops
- Lists
- String methods
- Boolean values
- Built-in functions (`any()`, `len()`)
- User input and output
- f-strings

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Run the following command:

```bash
python password_checker.py
```

## Strength Scoring

| Score | Classification |
|---|---|
| 0–2 | Weak |
| 3–4 | Moderate |
| 5 | Strong |

## Note

This is an educational, rule-based password strength checker. Its small common-password list and scoring rules are not a substitute for production-grade password security systems.