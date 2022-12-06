
def series_1(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def series_2(n, x):
    sum = 0
    for i in range(1, n+1):
        if(i%2==0):
            sum += x ** i
        else:
            sum -= x ** i
    return sum

def series_3(n):
    sum = 0
    for i in range(1, n+1):
        sum +=((i * (i + 1))/2)
    return sum

def fact(n):
    if n==1:
        return n
    else:
        return n * fact(n-1)

def series_4(n, x):
    sum = 1
    for i in range(1, n+1):
        if(i%2==0):
            sum+= (x ** i)/fact(i)
        else:
            sum-= (x ** i)/fact(i)
    return sum


#b

def enter_words():
    for i in range(0, 5):
        word = input("Enter a word: ")
        while(len(word) < 6):
           word = input("Enter a word with more than 5 characters: ")
        print("Entered word is : ",word)
           

#c

def ebill(units):
    price_tier1 = units * 3
    price_tier2 = 100 + units * 3.75
    price_tier3 = 250 + units * 4
    price_tier4 = 300 + units * 4.25
    price_tier5 = 400 + units * 5

    if(units >= 0 and units  <= 150):
        return price_tier1
    elif(units >=151 and units <=350):
        return price_tier2
    elif(units >=351 and units <= 450):
        return price_tier3
    elif(units >=451 and units <=600):
        return price_tier4
    else:
        return price_tier5

#d

from datetime import datetime
def get_hours_mins(entry_time, exit_time):
    """ Use only 24 hour format """

    entry_time+=":00"
    exit_time+=":00"

    FMT = "%H:%M:%S"
    tdelta = datetime.strptime(exit_time, FMT) - datetime.strptime(entry_time, FMT)
    [hh, mm, _] = str(tdelta).split(":")

    return [int(hh), int(mm)]

def parking(entry_time, exit_time, v_type):
    """
        Entry and Exit time should be in 24hr clock format
        v_type = "1 or 2 or 3"
        1 -> Truck/bus
        2 -> Car
        3 -> Cycle/Motor Cycle/Scooter
    """
    [hh, mm] = get_hours_mins(entry_time, exit_time)
    rate=0;
    if v_type==1:
        if hh <= 2 and mm <=59:
            rate=20
        else:
            rate=30
    elif v_type==2:
        if hh < 2 and mm <=59:
            rate=10
        else:
            rate=20
    elif v_type==3:
        if hh < 2 and mm <=59:
            rate=5
        else:
            rate=10
    else:
        print("Wrong Vechicle option")
    return rate


def parking_input():
    print("PARKING CHARGE CALCULATOR")
    print("Vehicle Types")
    print("1. Truck", "2. Car", "3. Cycle / Motor Cycle / Scooter", sep="\n")

    v_type = int(input("Enter Vehicle Type option (1/2/3): "))

    entry_time = input("Enter the entering time in 24hr clock format: ")
    exit_time = input("Enter the exiting time in 24hr clock format: ")
    
    result = parking(entry_time, exit_time, v_type)
    print(result)


#parking_input()


#e
import time
def str_to_num_arr(arr):
     return list(map(lambda s: int(s), arr))

def sanitize_date(date):
    date_arr=date.split("/")
    if(len(date_arr[-1]) == 2 ):
        date_arr[-1] = time.strptime(date, "%d/%m/%y").tm_year
    return str_to_num_arr(date_arr)


def calculate_age(current_date, birth_date):
    current_date = sanitize_date(current_date)
    birth_date = sanitize_date(birth_date)
    d = current_date[0] - birth_date[0]
    m = current_date[1] - birth_date[1]
    y = current_date[2] - birth_date[2]
    return [y, m ,d]

def display_age(age):
    print("You are {} years {} months and {} days old".format(age[0], age[1], age[2]))
    
##
##birth = input("Enter your birth date (dd/mm/yy): ")
##today = input("Enter today's date (dd/mm/yy): ")
##
##display_age(calculate_age(today, birth))
    
#patterns


#f
def display_month(month):
    if(month<0 or month >12):
        return
    months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
            ]
    return months[month-1]


#month_num = int(input("Enter month number: "))
#month = display_month(month_num)
#if(month==None):
#    print("Enter a valid month number")
#else:
#    print(month)


def pattern_g():

    length=0
    digits=""
    while(True):
        digits = input("Enter a five digit number: ")
        length=len(digits)

        if(length==5):
            break
    for i in range(1, length+1):
        print((i-1)*" ", digits[i-1:], digits[0:i])

# pattern_g()

def pattern_i(length):
    for i in range(0, length):
        for j in range(0, length):
            if((i==0 or i==length-1) or (j==0 or j==length-1)):
                print("* ", end="")
            else:
                print("  ", end="")
        print("")

def pattern_i2(length):
    for i in range(0, length):
        for j in range(0, length):
            if(j==i):
                print("$ ", end="")
            elif((i==0 or i==length-1) or (j==0 or j==length-1)):
                print("* ", end="")
            else:
                print("  ", end="")
        print("")
            
                
def pattern_i3(length):
    for i in range(0, length):
        for j in range(0, length):
            if(j==i or j==length-1-i):
                print("$ ", end="")
            elif((i==0 or i==length-1) or (j==0 or j==length-1)):
                print("* ", end="")
            else:
                print("  ", end="")
        print("")


def pattern_i4(length):
    for i in range(0, length):
        for j in range(0, length):
            if(j<=i-1):
                print("* ", end="")

        print("")
    for i in range(0, length):
        for j in range(0, length):
            if(j<=length-1-i):
                print("* ", end="")
        print("")

def pattern_i5(length):
    c=0
    for i in range(0, length):
        for j in range(c+1, 0, -1):
            print(j, end="")
        for k in range(1, c+1):
            print(k+1, end="")
                
        print("")
        c+=1

#pattern_i(12)
#pattern_i2(10)
#pattern_i3(10)
#pattern_i4(6)
#pattern_i5(5)

def seq1(n):
    for i in range(1, n+1):
        print(i**3, end=" ")
def seq2(n):
    for i in range(-n, 0):
        print(i+3, end =" ")
    for i in range(0, n):
        print(i*3, end=" ")


def seq3(n):
    for i in range(1, n+1):
        print(-i*2, end=" ")


def seq4(n):
    i, c = 1, 1
    while(i <= n):
        print(c, end=" ")
        c+=3
        i+=1

def wage():
    hourly_wage = int(input("Enter the hourly wage: "))
    regular_hrs = int(input("Enter total regular hours: "))
    overtime_hrs = int(input("Enter total overtime hours: "))

    weekly_pay = (hourly_wage * regular_hrs) + (overtime_hrs * 1.5 * hourly_wage)
    print("Total weekly pay is: ", weekly_pay)
