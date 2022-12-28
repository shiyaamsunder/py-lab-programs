def encrypt(message, key):
    encrypted_message=""
    for i in message:
        i=ord(i)+key
        if(i>90 and i<97):
            i=(i%90)+64
        elif(i>122):
            i=(i%122)+96
        encrypted_message+=chr(i)
    return encrypted_message


message = input("Enter message: ")
key= int(input("Enter key: "))
print("Encrypted message: " + encrypt(message, key))
