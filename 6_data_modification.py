
def modify_data(x, y=None, z="Hello"):
    if y is None:
        y = [1, 2, 3]  
    print(f"Initial x: {x}, y: {y}, z: {z}")

    x = x * 2
    y.reverse()
    z = z + " fazalullah"

    print(f"Modified x: {x}, y: {y}, z: {z}")

    return x, y, z

a = 5
b = [1, 2, 3]
c = "Hello"

modify_data(a, b, c)

print(f"Final a: {a}, b: {b}, c: {c}")
