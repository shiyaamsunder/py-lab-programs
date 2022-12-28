string = input("Enter a string: ")

result = ""

for i in range(0, len(string)):
    if i%2==0:
        result+=string[i]

print(result)
