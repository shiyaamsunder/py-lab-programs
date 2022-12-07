
def cel_far(temp):
    return temp * (9/5) + 32

celsius = float(input("Enter Celsius: "))
print("{} in Farenheit is {}".format(celsius, cel_far(celsius)))
