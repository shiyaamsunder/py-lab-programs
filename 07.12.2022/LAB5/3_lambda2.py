cube = lambda n: n * n  * n

def cal_cube(n, cube):
    return cube(n)

n = int(input("Enter a number: "))
print("Cube of {} is: {}".format(n, cal_cube(n, cube)))

