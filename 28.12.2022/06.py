string1 = input("Enter a string: ")
char = input("Enter a character: ")

flag = False
for i in range(0, len(string1)):
    if char == string1[i]:
        print(char + " is present at position " + str(i+1))
        flag=True

if(flag==False):
    print(char + " is not present")
