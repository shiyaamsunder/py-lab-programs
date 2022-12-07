def fib_recurse(n):
    pass

def fib_iterative(n):
    a,b=0,1
    print(a)
    print(b)
    
    for i in range(0, n+1):
        c=a+b
        print(c)
        a=b
        b=c

fib_recurse(10)
