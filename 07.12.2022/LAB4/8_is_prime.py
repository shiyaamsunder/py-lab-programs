def is_prime(n):
    if(n==2): return 1
    flag=1
    for i in range(2, int(math.sqrt(n))):
        if (n%i==0):
            flag=0
            break

    return flag

n = int(input("Enter a number: "))
print(is_prime(n))
