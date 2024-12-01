import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

a = int(input("Enter the first number: "))

b = int(input("Enter the second number: "))

print(f"The LCM of {a} and {b} is {lcm(a, b)}")
