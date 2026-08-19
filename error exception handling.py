try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Division by zero is not possible.")
except ValueError:
    print("Input should only be digits.")