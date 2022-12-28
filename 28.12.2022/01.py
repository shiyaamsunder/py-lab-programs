
def check_pan(pan):
    pan_status = set("P,C,H,A,B,G,J,L,F,I")

    
    if(len(pan)!=10):
        print("PAN number should be ten-digit alphanumeric number")
        return

    if(pan_number[0:2].isdigit()):
        print("First three characters should be alphabets")
        return

    if(pan_number[3] not in pan_status):
        print("Fourth character should be one of these characters: " + pan_status)
        return

    if(pan_number[4] != name[0].upper()):
        print("Fifth character does'nt match the first character of the name")
        return
    
    if(pan_number[5:8].isalpha() and pan_number[-1].isdigit()):
        print("Last five characters should contain 4 digits and one alphabet")
        return

    print("Valid PAN number")

name = input("Enter your name: ")
pan_number = input("Enter your PAN number: ")


if(name.isdigit()):
    print("Name should not contain any numbers")

check_pan(pan_number)
