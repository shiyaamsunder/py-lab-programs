def fib_recurse(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_recurse(n-1)+fib_recurse(n-2)

def fib_iterative(n):
    a,b=0,1
    print(a, end= " ")
    print(b, end= " ")

    
    i=0
    while(i<n-2):
        c=a+b
        a=b
        b=c
        print(c, end= " ")
        i+=1


n = int(input("Enter n: "))


print("Using recursion")
for i in range(0, n):
    print(fib_recurse(i), end=" ")

print("")

print("Using iteration")
fib_iterative(n)
