def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) 

num1 = int(input("Enter a number: "))

if num1 < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num1)  
    print(f"Factorial of {num1} is: {result}") 