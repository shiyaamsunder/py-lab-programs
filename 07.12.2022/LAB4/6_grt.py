def greatest_three(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c):
        return b
    else:
        return c

print(greatest_three(10,1,2))
