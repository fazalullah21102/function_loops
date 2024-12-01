def person(name, *traits, **details):
 print(f"Name: {name}")
 print("Traits:")
 for trait in traits:
    print(f"- {trait}")
 print("Details:")
 for key, value in details.items():
    print(f"{key}: {value}")
person(
 "Fazalullah",
 "Kind", "Hardworking", 
 age=20, country="Pakistan", hobby="Programming"
)
