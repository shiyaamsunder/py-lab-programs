import math
# def isPrime(n):
#     if n==2: return True
#     flag=0
#     for i in range(3, int(math.sqrt(n))+1):
#         if(n%i==0):
#             flag=1
#             break
#
#     if(flag==1):return False
#     return True
#
#
# print(isPrime(9))


# c = input("Enter a character: ")
# a = ord(c)
# print("ASCII value of {} is {}".format(c, a))

def sumOfSquares(n):
    return (n*(n+1)*(2*n+1))/6


def sumOfCubes(n):
    return int(math.pow((n*(n+1)/2), 2))


def sumsq(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*i

    return sum


def isPositive(n):
    return True if n > 0 else False


def isLeapYear(y):
    if (y % 4 == 0 or (y % 100 != 0 and y % 400 == 0)):
        return True
    else:
        return False


def isEven(n):
    return n % 2 == 0


def decToBin(n):
    b = []
    i = 0
    while n != 0:
        rem = n % 2
        b.append(str(rem))
        i = i+1
        n = n//2

    b.reverse()
    return "".join(b)


def fact(n):
    return n if n == 1 else n * fact(n-1)


e = 0
v = 0
while True:
    n = int(input("Enter: "))
    if (n == -1):
        break 
    if (n % 2 == 0):
        e = e + 1
    else:
        v = v + 1
print("Even {} Odd {}".format(e, v))
