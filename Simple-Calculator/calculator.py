# calculator.py
# __author__ = faroukadekunle001@gmail.com || Github: @farookie007
# Write a Python calculator that can perform: addition, subtraction, division, multiplication and modulus operations.
# It should accept user input


# Simple CLI Calculator
import sys


def addition(num1, num2):
    # returns the sum of num1 and num2
    return num1 + num2


def subtraction(num1, num2):
    # returns the difference of num1 and num2
    return num1 - num2


def division(num1, num2):
    # divide num1 by num2 and returns the result
    return num1 / num2


def multiplication(num1, num2):
    # returns the product of num1 and num2
    return num1 * num2


def modulus(num1, num2):
    # returns the remainder when num1 is divided by num2. The result is an integer
    return num1 % num2


def _format_answer(num1, num2, operator, result):
    # this function helps format the arithmetic expression
    def prettify(num):
        return int(num) if num == round(num, 0) else num
    return f"{prettify(num1)} {operator} {prettify(num2)} = {prettify(result)}"


def calculator():
    operations = [sys.exit, addition, subtraction, division, multiplication, modulus]   # mapping each operation to certain index
    # matching each arithmeticds operation to their operators
    operators = {
        addition : '+',
        subtraction : '-',
        division : '/',
        multiplication : '*',
        modulus : '%'
    }


    user_choice = True
    while user_choice:
        print("******* SIMPLE CALCULATOR *******")
        try:
            # converting the user input to float as float could accomodate integers also
            num1 = float( input("First Number: ") )
            num2 = float( input("Second Number: ") )
            print("""
            Which of the following operations would you like to perform:
                1. Addition
                2. Subtraction
                3. Division
                4. Multiplication
                5. Modulus

                0. Quit
            """)
            
            # converting `user_choice` to positive integer to match each corresponding `operations` index
            user_choice = abs( int( input("Reply with the corresponding number: ") ) )
            action = operations[user_choice]
            operator = operators.get(action)    # using the get method to handle error when `user_choice` is 0
            if user_choice:     # will only be true if `user_choice` is not 0
                result = _format_answer(num1, num2, operator, action(num1, num2))
                print()
                print("-" * len(result))
                print(result)
                print("-" * len(result))
                print()
            else:
                print("[-] Terminating...")
                action()

        except (ValueError, KeyError):
            print("[Error]: Invalid entry. Try Again")
            user_choice = True
            continue
        print()


if __name__ == '__main__':
    calculator()