"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A `ValueError` occurs when a function receives an argument of the correct type but an inappropriate value, such as
providing a string or float when an integer is expected.
2. When will a ZeroDivisionError occur?
A `ZeroDivisionError` occurs when dividing a number by zero, such as in `928 / 0`.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, I can change the code to check if the denominator is zero before performing the division. This way, I can avoid
 the `ZeroDivisionError`.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")