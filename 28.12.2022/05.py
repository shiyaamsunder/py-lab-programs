string = input("Enter a string: ")

vowels = set("aieou")
result=""
for i in string:
    if i in vowels:
        continue
    else:
        result+=i
print(result)
