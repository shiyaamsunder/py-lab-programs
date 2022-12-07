def compound_interest(p, n ,r):
    return (p * (1 + (r/100))**n ) - p
    

p=float(input("Enter Principal: "))
n=float(input("Enter number of years: "))
r=float(input("Enter the rate of interest: "))

print("CI is:", compound_interest(p,n,r))
