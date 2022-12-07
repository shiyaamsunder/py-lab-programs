def reverse(n, r):
    if n==0:
        return r
    else:
        return reverse(n//10, r*10+ n%10)

n = int(input("Enter a number:"))

print(reverse(n, 0))
              
        
