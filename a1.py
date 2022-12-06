# utils
def get_input_arr(msg):
    nums = input(msg)
    nums=map(lambda str_num: int(str_num), nums.split(" "))
    return list(nums)

# Reverse three digit number

def reverse(n):
    reversed=""
    while(n!=0):
        reversed+=str(n%10)
        n//=10
    return int(reversed)

#n=int(input("Enter a number: "))
#print("Reversed ", reverse(n))

def armstrong(n):
    digits=0
    temp=n
    remainder=0
    result=0

    while(temp!=0):
        temp//=10
        digits+=1
    
    temp=n
    
    while(temp!=0):
        remainder=temp%10
        result+= remainder ** digits
        temp//=10
 
    if(result==n):
        return True
    else:
        return False


#n = int(input("Enter a number: "))
#print("Is an armstrong number") if(armstrong(n)) else print("Not an armstrong number")

def sum_array(arr):
    sum=0
    for i in range(0, len(arr)):
        sum+=arr[i]
    return sum

#nums = input("Enter numbers seperated by space: ")
#nums=map(lambda str_num: int(str_num), nums.split(" "))
#print(sum_array(list(nums)))

def count_odd_even(arr):
    [odd, even]=[0, 0]
    for i in range(0, len(arr)):
        if(arr[i] % 2 == 0):
            even+=1
        else:
            odd+=1
    return [odd, even]


#nums = get_input_arr("Enter numbers seperated by space: ")
#count = count_odd_even(nums)
#print("Odd count %d, Even Count %d" % (count[0], count[1]))
import time
def timer():
    total = 1 * 60 * 60 
    print("Exam Started")
    while total >= 0:
        print(str(total // 60) + " mins left")
        time.sleep(60)

        total-=60
    print("\nExam Over")


#timer()


max_weight_metric = 635
max_height_metric = 272

max_weight_imp = 1400
max_height_imp = 107

def is_valid_metric(w, h):
    return w < max_weight_metric and h < max_height_metric


def is_valid_imp(w, h):
    return w < max_weight_imp and h < max_height_imp

def calculate_bmi(w, h, is_imp):
    return (w / h ** 2) * 703 if is_imp else w / h ** 2

def check_bmi(bmi):
    if bmi <= 15:
        print("Severely Underweight")
    elif bmi <= 18.5:
        print("Underweight")
    elif bmi > 18.5 and bmi <= 25:
        print("Normal")
    elif bmi > 25 and bmi <= 39.9:
        print("Overweight")
    else:
        print("Obese")


def get_bmi_input():
    print("BMI Calculator")
    print("Which unit system you want to use?\n1.Metric System (kg and cm)\n2.Imperial System (pounds and inches)")
    unit_sys = int(input("Enter option (1/2): "))
    bmi = 0 

    if(unit_sys==1):
        w = float(input("Enter weight in kg: "))
        h = float(input("Enter height in cm: "))
        if(is_valid_metric(w, h)==False):
            print("Enter valid weight or height")
            return
        bmi = calculate_bmi(w, h/100, False)
    elif(unit_sys==2):
        w = float(input("Enter weight in pounds: "))
        h = float(input("Enter height in inches: "))
        if(is_valid_imp(w, h)==False):
            print("Enter valid weight or height")
            return
        bmi = calculate_bmi(w, h, True)
    else:
        print("Enter valid option")
        return
    print(bmi)
    check_bmi(bmi)


get_bmi_input()







