
def calculate_power(base, exponent):

    result = base ** exponent
    return result

def main():
  
    base = 5
    exponent = 3
    
    result = calculate_power(base, exponent)
    
    print(f"{base}^{exponent} = {result}")

if __name__ == "__main__":
    main()
