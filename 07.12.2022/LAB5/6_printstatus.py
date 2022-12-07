def print_status(status):
    """
    This function returns the appropriate message based the status passed in.
    """
    status = status.upper()
    if(status=="S"):
        print("Seperated")
    elif(status=="M"):
        print("Married")
    elif(status=="D"):
        print("Divorced")
    elif(status=="U"):
        print("Unmarried")
    else:
        print("Enter proper status message. It can only be 'S', 'M', 'D' or 'U'")


print_status("a")
