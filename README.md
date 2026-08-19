# Python Exception Handling

## Overview

This project demonstrates exception handling in Python using `try` and `except` blocks. The program accepts two numbers from the user and performs division while handling common input and calculation errors.

## Program Description

The program:

1. Accepts two integer values from the user.
2. Divides the first number by the second number.
3. Displays the result if the operation is successful.
4. Handles division by zero using `ZeroDivisionError`.
5. Handles invalid input using `ValueError`.

## Exception Handling

### ZeroDivisionError

If the user enters `0` as the second number, division cannot be performed.

Example:

```text
Enter a number: 10
Enter another number: 0
Division by zero is not possible.
```

### ValueError

If the user enters a value that cannot be converted into an integer, the program displays an error message.

Example:

```text
Enter a number: abc
Enter another number: 5
Input should only be digits.
```

## Sample Output

### Valid Input

```text
Enter a number: 20
Enter another number: 4
5.0
```

### Division by Zero

```text
Enter a number: 20
Enter another number: 0
Division by zero is not possible.
```

### Invalid Input

```text
Enter a number: abc
Enter another number: 5
Input should only be digits.
```

## Concepts Covered

* Python Exception Handling
* `try` and `except`
* `ZeroDivisionError`
* `ValueError`
* User Input
* Type Conversion
* Arithmetic Operations
* Error Handling

## Requirements

* Python 3.x
* No external libraries are required.

## How to Run

Save the program in a Python file, for example:

```text
exception_handling.py
```

Run the program using:

```bash
python exception_handling.py
```

## Project Structure

```text
Python_Exception_Handling/
├── exception_handling.py
└── README.md
```

Replace `exception_handling.py` with the actual filename if it is different.

## Author

Kotapati Dhananjay

GitHub: https://github.com/KotapatiDhananjay
