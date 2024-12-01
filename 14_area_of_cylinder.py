def area_of_cylinder(radius, height):
    
    pi = 3.14159  # Value of π
    area = pi * radius**2 * height 
    return area
    
radius = float(input("Enter the radius of the cylinder: "))

height = float(input("Enter the height of the cylinder: "))

cylinder_area = area_of_cylinder(radius, height)

print("The area of the cylinder is:", cylinder_area)
