words  = ["able", "apple", "acid", "across", "add", "alarm", "air", "ball", "beauty", "bank", "bakery", "being", "begin", "cat", "child", "check", "coast", "combust", "cipher", "cross", "dog", "dance", "dark", "desert", "describe", "deposit", "experiment", "elephant", "express", "equal", "entrance"]

letter = input("Enter a character: ")
if (len(letter) > 1):
    print("Enter a single character")
elif(letter.isdigit()):
     print("Enter an alphabet")

for i in words:
    if(i.startswith(letter)):
        print(i)
