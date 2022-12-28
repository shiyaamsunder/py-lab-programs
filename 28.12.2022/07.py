string = input("Enter a string: ")
char = input("Enter a character: ")

found = False
count = 0
for i in string:
    if i==char:
        count+=1
        found=True

if(found==False):
    print(f"Character '{char}' is not present")
else:
    print(f"Character '{char}' occurs {count} times")
