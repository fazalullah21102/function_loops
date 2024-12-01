
numbers = [3, 5, 7, 8, 11, 14]

for num in numbers:
    if num % 2 == 0: 
        print(f"First even number found: {num}")
        break  
    print(f"{num} is not even")
