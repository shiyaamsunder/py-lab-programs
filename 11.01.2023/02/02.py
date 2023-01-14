bdays = {"paul": "19/09/1996", "eren": "22/01/1999", "matt": "24/04/1985"}

name = input("Enter name: ").lower()

if name not in bdays:
    bday = input("Name is not available. Please enter bday to add: ")
    bdays[name] = bday
else:
    print(bdays[name])

print(bdays)

