def swap():
    global a
    global b

    a=10
    b=20
    print("Before swapping: ", a,b)
    a,b=b,a
    print("After swapping: ", a,b)

swap()
print(a, b)
