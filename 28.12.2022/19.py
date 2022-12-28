string = input("Enter a string: ")


lowercase_min = 97
lowercase_max = 122
uppercase_min = 65
uppercase_max = 90
special_chars = set("!@#$%^&*()-_")

digit_count = 0
lchar_count = 0
uchar_count = 0
schar_count = 0


for i in string:
    if i.isdigit():
        digit_count+=1
    elif i.isalpha():
        if(ord(i) >= 97 and ord(i) <=122):
            lchar_count+=1
        elif(ord(i) >=65 and ord(i) <=90):
            uchar_count+=1
    elif(i in special_chars):
        schar_count+=1

            
print(f"Lowercase:  {lchar_count}")
print(f"Uppercase: {uchar_count}")
print(f"Special Char: {schar_count}")
print(f"digits: {digit_count}")
