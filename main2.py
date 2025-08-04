'''This is a programme to print the factorial of the number inputer by the user.'''
print("This is a programme to print the factorial of the number by Abhay14-python.")
while True:
    try:
        n = int(input("Enter the number which you have to find the factorial of : "))
        break
    except Exception:
        print("Invalid input \n Please enter a valid input")

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

if n < 0:
    print("Factorial does not exist for negative numbers.")
else :

    print(f"The factorial of {n} is {factorial(n)}")
