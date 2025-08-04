'''This is a programme to print the factorial of the number inputer by the user.'''
print("This is a programme to print the factorial of the number by - Abhay12-python.")
while True:
    try:
        n = int(input("Enter the number which you have to find the factorial of : "))
        break
    except Exception:
        print("Invalid input \n Please enter a valid input")
factorial = 1
if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1")
elif  n == 1:
    print("The factorial of 1 is 1")
else :
    for i in range(1,n+1):
        factorial *= i
    print(f"The factorial of {n} is {factorial}")


