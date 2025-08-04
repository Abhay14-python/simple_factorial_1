'''This is a programme to print the factorial of the number inputer by the user.'''
print("This is a programme to print the factorial of the number by Abhay14-python.")
while True:
    try:
        n = int(input("Enter the number which you have to find the factorial of : "))
        break
    except Exception:
        print("Invalid input \n Please enter a valid input")

import math

factorial = math.factorial(n)
print(f"The factorial of the the number {n} is {factorial}")