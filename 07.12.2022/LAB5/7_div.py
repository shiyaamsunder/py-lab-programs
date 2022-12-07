def divisible(m,n):
    nums = []
    for i in range(1, n+1):
        if(i%m==0):
            nums.append(i)
    return nums

m = int(input("Enter m: "))
n = int(input("Enter n (Should be greater than m): "))

nums = divisible(m, n)
for i in nums:
    print(i)
