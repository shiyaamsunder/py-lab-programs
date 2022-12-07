
#default
def required(a, b=10):
    return a+b

#keyworded
def keyworded(a, b):
    return a+b

#arbitrary
def arbitrary(*args):
    for arg in args:
        print(arg)
