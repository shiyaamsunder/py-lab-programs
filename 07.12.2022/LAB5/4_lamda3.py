compute = lambda n: compute(n/2) + 1 if n>1 else n

n = int(input("Enter a number: "))
print(compute(n))
