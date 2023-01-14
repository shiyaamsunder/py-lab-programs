employee_details = [
        {
            "name": "Matt",
            "age": 32,
            "role": "Tester",
            "address": {
                "flat_no": "A1", 
                "street": "New street",
                "city": "Chennai",
                "pincode": "600010" 
             }
        },
        {
            "name": "John",
            "age": 38,
            "role": "Manager",
            "address": {
                "flat_no": "A1", 
                "street": "New street",
                "city": "Chennai",
                "pincode": "600010" 
             }
        },
        {
            "name": "Eren",
            "age": 22,
            "role": "Engineer",
            "address": {
                "flat_no": "A1", 
                "street": "New street",
                "city": "Chennai",
                "pincode": "600010" 
             }
        },
    ]


print("--------------------------------------------------------")
print(f'{"NAME":<20}{"AGE":<10}{"ROLE":<16}CITY')
print("--------------------------------------------------------")
for emp in employee_details:
    print(f'{emp["name"]:<20}{emp["age"]:<10}{emp["role"]:<16}{emp["address"]["city"]}\n')
