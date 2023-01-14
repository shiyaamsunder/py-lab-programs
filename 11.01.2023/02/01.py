products = []


def get_product():
    name =  input("Enter name: ")
    price = float(input("Enter price: "))

    products.append({"name": name, "price": price})


def calculate_bill():
    total = 0
    for product in products:
        total+=product["price"]
    return total


def display_bill(total):
    print("------------------------------------------------")
    print(f'{"PRODUCT":<36}{"PRICE"}')
    for product in products:
        print(f'{product["name"]:<36}{product["price"]}')
    print("------------------------------------------------")
    print(f'{"TOTAL":>35}',  round(total, 2))


while(True):
    print("\n1. Enter product name and MRP")
    print("\n2. Calculate and display bill")
    print("Enter -1 to exit")
    print("\n\n")

    choice = int(input("Enter choice: "))

    if(choice == -1):
        break

    if(choice == 1):
        get_product()

    elif(choice == 2):
        total = calculate_bill()
        display_bill(total)




