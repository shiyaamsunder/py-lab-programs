string = input("Enter a string: ")

reverse = []
for i in string.split(" "):
        reverse.append(i[::-1])

reverse=" ".join(reverse)
        
print(f"Reversed string is: {reverse}")
