def is_leap_year(year):
    if(year%100==0 and year%400==0):
        print("Leap year")
    elif(year%100!=0 and year%4==0):
        print("Leap year")
    else:
        print("Not a leap year")

year = int(input("Enter a year: "))
is_leap_year(year)
