string = input("Enter a string: ")

def reverse_string(string):
    reverse = []
    for i in string.split(" "):
            reverse.append(i[::-1])

    return " ".join(reverse)
        
if(string==reverse_string(string)):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
