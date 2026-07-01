# Error Handling Practice

I created this small project to practise handling common errors in Python.

The program gives the user two options. It can divide two numbers or try to open a text file. Instead of stopping when something goes wrong, it displays a clear message explaining the problem.

## What the Program Does

- Divides two numbers
- Handles division by zero
- Handles letters or other invalid number entries
- Opens and reads a text file
- Handles missing files
- Handles file permission errors
- Handles an invalid menu choice

## Project File

- `error_examples.py` contains the Python program

## How to Run It

From the main repository folder, run:

```bash
python error-handling/error_examples.py
```

## Tests I Tried

I tested the program by:

- Dividing `10` by `0`
- Entering letters instead of numbers
- Entering the name of a file that does not exist
- Choosing an option outside the menu

## What I Learned

While working on this project, I learned how to:

- Use `try` and `except`
- Handle `ValueError`
- Handle `ZeroDivisionError`
- Handle `FileNotFoundError`
- Handle `PermissionError`
- Show helpful messages instead of allowing the program to crash