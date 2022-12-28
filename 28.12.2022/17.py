string = input("Enter a string: ")
chars = input("Enter a set of chars: ")

if chars not in string:
    print(string)
else:
    for i in chars:
        string=string.replace(i, "")
    print(string)
