a = int(input ("enter a ; "))
def data(first_name, last_name, age=None, country="Unknown"):
    
    print("First Name:" , first_name, "Last Name:" , last_name, "Age:", age, 
"Country:" ,country)

data("Fazalullah", "Ali")

data("Fazalullah", "Ali", age=20)

data(first_name="Ali", last_name="Zaid", age=25, country="Pakistan")
