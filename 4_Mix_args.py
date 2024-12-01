def person (name , age ,address , *subject):
    print(f"name: {name} age: { age } address :{address}")
    print("total subject : ")
    for subject1 in subject:
        print(subject1)
person("fazalullah" , 18  , "peshawar" , "DSA" , "AI" , "operation system " , "s/w engenner" , "etc")