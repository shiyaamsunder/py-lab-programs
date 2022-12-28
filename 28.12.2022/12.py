def a(message):
##    result=""
##    for i in range(0, len(message)):
##        if i==0:
##            result+=message[i].upper()
##        else:
##            result+=message[i]
##    return result
    return message.capitalize()

def b(message):
    message=message.split(" ")
    result=list(map(a, message))
    return " ".join(result)
    
def c(message):

##    def change_case(m):
##        r = ""
##        for i in m:
##            if i.isupper():
##                r+=i.lower()
##            else:
##                r+=i.upper()
##        return r
##
##    message=message.split(" ")
##    result=list(map(change_case, message))
##    return " ".join(result)
    return message.swapcase()

def d(message):
    message = a(message)
    message = message.replace("world", "Friends")
    return message

message = input("Enter message: ")

print(d(message))
